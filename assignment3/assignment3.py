import pandas as pd

people_dict = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' :  [25, 30, 35],
    'City' :  ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(people_dict)

print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

task1_older.to_csv('employees.csv', index=False)
df = pd.read_csv('employees.csv')
print(df)

task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

json_employees = pd.read_json('additional_employees.json')
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

print(more_employees.info)