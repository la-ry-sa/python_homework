import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    myDict = {}
    myRows = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    myDict['fields'] = row
                    first = False
                else:
                    myRows.append(row)
            myDict['rows'] = myRows
        return myDict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

def column_index(field):
    return employees["fields"].index(field)

employee_id_column = column_index("employee_id")

def first_name(row_num):
    index = column_index("first_name")
    return employees["rows"][row_num][index]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

def employee_find_2(employee_id): 
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

def sort_by_last_name():
    employees["rows"].sort(key= lambda row : row[column_index("last_name")])
    return employees["rows"]

def employee_dict(row):
    employee_zip = zip(employees["fields"], row)
    emp_dict = {}
    for key, value in employee_zip:
        if key != "employee_id":
            emp_dict[key] = value
    return emp_dict

print(employee_dict(employees["rows"][2]))

def all_employees_dict():
    all_emp_dict = {}
    for row in employees["rows"]:
        all_emp_dict[row[column_index("employee_id")]] = employee_dict(row)
    return all_emp_dict

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(secret):
    custom_module.set_secret(secret)

print(custom_module.secret)

def read_minutes():
    def read_file(filename):
        with open (f"../csv/{filename}.csv", "r") as file:
            reader = csv.reader(file)
            first = True
            result = {}
            result["rows"] = []
            for row in reader:
                if first:
                    result["fields"] = row
                    first = False
                else:
                    result["rows"].append((tuple(row)))
        return result
    minutes1 = read_file("minutes1")
    minutes2 = read_file("minutes2")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print(minutes_set)

def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))

minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    formatted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open("../minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in formatted_list:
            writer.writerow(row)
    return formatted_list

write_sorted_list()