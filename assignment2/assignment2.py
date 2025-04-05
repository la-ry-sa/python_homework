import sys
import csv

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

print(employee_dict(employees['rows'][1]))