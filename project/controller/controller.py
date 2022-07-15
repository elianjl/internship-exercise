__author__ = "elianjl"
from model.model import Employee
from view.view import print_coincidences


def read_file(file_name):
    # return an array of strings with information of the employees
    with open(file_name) as file_obj:
        lines = file_obj.readlines()
        return lines


def list_employee(lines):
    # return an array of Employee's object given an array of strings with information of the employees
    employees = []
    for i in lines:
        employee = i.split("=")
        employees.append(Employee(employee[0], employee[1].split(",")))
    return employees


def compare_schedule(first_checkin, first_checkout, second_checkin, second_checkout):
    # compare each case when the employees coincidence at the office in the same time
    flag = False
    if first_checkin <= second_checkin and first_checkout >= second_checkin:
        if first_checkin <= second_checkout and first_checkout >= second_checkout:
            if first_checkin >= second_checkin and first_checkout <= second_checkout:
                flag = True
    return flag


def count_coincidence(employees):
    # return the number of coincidences given the list of employees
    coincidences = []
    for i in range(len(employees)):
        employee = employees[i]
        for j in range(i+1, len(employees)):
            cont = 0
            next_employee = employees[j]
            for day_employee in employee.schedule:
                for day_next_employee in next_employee.schedule:
                    if day_employee[0:2] == day_next_employee[0:2]:
                        if compare_schedule(day_employee[2:7], day_employee[8:13], day_next_employee[2:7], day_next_employee[8:13]):
                            cont += 1
            coincidences.append(
                f"{employee.name}-{next_employee.name}: {cont}")
    return coincidences


def call_view():
    # print the coincidences
    file_name = 'data/data.txt'
    lines = read_file(file_name)
    employees = list_employee(lines)
    coincidences = count_coincidence(employees)
    print_coincidences(coincidences)
