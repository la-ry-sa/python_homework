import sqlite3
import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
employees = pd.read_csv("employees.csv")

with sqlite3.connect("../db/lesson.db") as conn:
    orders.to_sql("orders", conn, if_exists="replace", index=False)
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    employees.to_sql("employees", conn, if_exists="replace", index=False)

    cursor = conn.cursor()

    conn.execute("PRAGMA foreign_keys = 1")

# Find the total price of each of the first 5 orders. There are several steps.  
# You need to join the orders table with the line_items table and the products table.  
# You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of 
# the product price times the line_item quantity.  
# Then, you ORDER BY order_id and LIMIT 5.

    cursor.execute("""SELECT orders.order_id,
                   ROUND(SUM(products.price * line_items.quantity), 2) AS total_price
                   FROM line_items
                   JOIN orders ON line_items.order_id = orders.order_id
                   JOIN products ON line_items.product_id = products.product_id
                   GROUP BY orders.order_id
                   ORDER BY orders.order_id
                   LIMIT 5
                   """)
    print(cursor.fetchall())

    # For each customer, find the average price of their orders.  This can be done with a subquery. 
# You compute the price of each order as in part 1, but you return the customer_id and the total_price.  
# That's the subquery. You need to return the total price using AS total_price, and you need to return 
# the customer_id with AS customer_id_b, for reasons that will be clear in a moment.  
# In your main statement, you left join the customer table with the results of the subquery, using ON 
# customer_id = customer_id_b.  You aliased the customer_id column in the subquery so that the column 
# names wouldn't collide.  Then group by customer_id -- this GROUP BY comes after the subquery -- and 
# get the average of the total price of the customer orders.  Return the customer name and the 
# average_total_price.

    cursor.execute("""
                   SELECT customers.customer_name, 
                   ROUND(AVG(total_price), 2) AS average_total_price
                   FROM customers
                   LEFT JOIN (SELECT orders.customer_id AS customer_id_b, 
                   ROUND(SUM(products.price * line_items.quantity), 2) AS total_price
                   FROM line_items
                   JOIN orders ON line_items.order_id = orders.order_id
                   JOIN products ON line_items.product_id = products.product_id
                   GROUP BY orders.order_id) AS order_totals
                   ON customers.customer_id = order_totals.customer_id_b
                   GROUP BY customers.customer_id
                   ORDER BY customers.customer_name
                   """)
    print(cursor.fetchall())

    # You want to create a new order for the customer named Perez and Sons.  The employee creating 
# the order is Miranda Harris.  The customer wants 10 of each of the 5 least expensive products.  
# You first need to do a SELECT statement to retrieve the customer_id, another to retrieve the 
# product_ids of the 5 least expensive products, and another to retrieve the employee_id.  
# Then, you create the order record and the 5 line_item records comprising the order.  
# You have to use the customer_id, employee_id, and product_id values you obtained from the 
# SELECT statements. You have to use the order_id for the order record you created in the 
# line_items records. The inserts must occur within the scope of one transaction. 
# Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along 
# with the quantity and product name for each.

    cursor.execute("""
                   INSERT INTO orders (customer_id, employee_id, date)
                   VALUES ((SELECT customer_id
                   FROM customers
                   WHERE customer_name = 'Perez and Sons'), 
                   (SELECT employee_id 
                   FROM employees
                   WHERE first_name = 'Miranda'
                   AND last_name = 'Harris'),
                   current_date)
                   RETURNING order_id
                   """)

    order_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")

    cheapest_products = cursor.fetchall()

    for product in cheapest_products:
        cursor.execute("""INSERT INTO line_items (order_id, product_id, quantity)
                   VALUES (?, ?, ?)""",
                   (order_id, product[0], 10))

    cursor.execute("""SELECT line_items.line_item_id,
                    line_items.quantity,
                    products.product_name
                    FROM line_items
                    JOIN products ON line_items.product_id = products.product_id
                    WHERE line_items.order_id = ?
                    """,
                   (order_id,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.commit()

# Find all employees associated with more than 5 orders.  You want the first_name, the last_name, 
# and the count of orders.  You need to do a JOIN on the employees and orders tables, and then 
# use GROUP BY, COUNT, and HAVING.

    cursor.execute("""SELECT emp.first_name, 
                   emp.last_name,
                   COUNT(order_id) AS number_of_orders
                   FROM employees emp
                   JOIN orders on emp.employee_id = orders.employee_id
                   GROUP BY emp.employee_id
                   HAVING COUNT(orders.order_id) > 5
                                             """)

    print(cursor.fetchall())