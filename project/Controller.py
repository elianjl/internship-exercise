from Model import Employee

def schedule(first_checkin, first_checkout, second_checkin, second_checkout):
    if (first_checkin <= second_checkin and first_checkout >= second_checkin) or (first_checkin <= second_checkout and first_checkout >= second_checkout) or (first_checkin >= second_checkin and first_checkout <= second_checkout):
        return True
    else:
        return False

def file_manage(file_name):

    with open(file_name) as file_obj:
        lines = file_obj.readlines()
    for i in lines:
        employee = i.split("=")
        employees.append(Employee(employee[0], employee[1].split(",")))

employees = []
file_name = 'data.txt'

file_manage(file_name)

for j in range(len(employees)):
    employee = employees[j]
    for k in range(j+1, len(employees)):
        cont = 0
        second_employee = employees[k]
        for l in range(len(employee.schedule)):
            for m in range(len(second_employee.schedule)):
                day = employee.schedule[l]
                day_other = second_employee.schedule[m]
                if day[0:2] == day_other[0:2]:
                    if schedule(day[2:7], day[8:13], day_other[2:7], day_other[8:13]) == True:
                        cont+=1
        print(employee.name, "-", second_employee.name, ":", cont)







    