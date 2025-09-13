import pandas as pd
import sqlite3

line_items = pd.read_csv("line_items.csv")
products = pd.read_csv("products.csv")

with sqlite3.connect("../db/lesson.db") as conn:
    line_items.to_sql("line_items", conn, if_exists="replace", index=False)
    products.to_sql("products", conn, if_exists="replace", index=False)
    sql_statement = """SELECT li.line_item_id, li.quantity, products.product_id, products.product_name, 
    products.price FROM line_items li JOIN products ON li.product_id = products.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))
    df['total'] = df['quantity'] * df['price']
    print(df.head(5))
    grouped_df = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'}).reset_index()
    grouped_df = grouped_df.sort_values(by='product_name')
    print(grouped_df.head(5))
    grouped_df.to_csv("../assignment8/order_summary.csv", index=False)