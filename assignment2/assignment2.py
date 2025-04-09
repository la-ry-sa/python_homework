import sys
import csv
import os
import custom_module
from datetime import datetime

def read_employees():
    my_dict = {}
    my_list = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    my_dict['fields'] = row
                else:
                    my_list.append(row)
            my_dict['rows'] = my_list

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return my_dict

def column_index(column):
    return employees['fields'].index(column)

def first_name(row_num):
    index = column_index('first_name')
    return employees['rows'][row_num][index]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

def sort_by_last_name():
    last_name_index = column_index('last_name')
    employees['rows'].sort(key=lambda row: row[last_name_index].strip())
    return employees['rows']

def employee_dict(row):
    result = {}
    for i, field in enumerate(employees['fields']):
        if field != 'employee_id':
            result[field] = row[i]
    return result

employees = read_employees()
employee_id_column = employees['fields'].index('employee_id')

def all_employees_dict():
    result = {}
    for row in employees['rows']:
        employee_id = row[0]
        result[employee_id] = employee_dict(row)
    return result

def get_this_value():
    return os.getenv('THISVALUE')

def set_that_secret(update_secret):
    return custom_module.set_secret(update_secret)

def read_minutes():
    def read_minutes_file(filename):
        with open(f'../csv/{filename}.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            result = {}
            result['rows'] = []
            for index, row in enumerate(reader):
                if index == 0:
                    result['fields'] = row
                else:
                    result['rows'].append(tuple(row))
        return result
    minutes1 = read_minutes_file('minutes1')
    minutes2 = read_minutes_file('minutes2')
    return minutes1, minutes2

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    return set1 | set2
    
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in formatted_list:
            writer.writerow(row)
    return formatted_list

set_that_secret('Kuku')
print(custom_module.secret)

print(employee_dict(employees['rows'][3]))

emp_dict = all_employees_dict()
print(emp_dict["10"])

minutes1, minutes2 = read_minutes()

m1, m2 = read_minutes()
print("First row from minutes1:", m1["rows"][0])

minutes_set = create_minutes_set()

minutes_list = create_minutes_list()