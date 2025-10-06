import csv

csv_path = "csv/employees.csv"
employees = []

with open(csv_path, newline='') as file:
    reader = csv.reader(file)
    employees = [row for row in reader]

employee_names = [f"{row[1]} {row[2]}" for row in employees[1:]]

print(employee_names)

e_names = [name for name in employee_names if 'e' in name.lower()]

print(e_names)