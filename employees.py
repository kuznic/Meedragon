import json,random,hashlib, binascii, os
class Employees():
    """This class details information about the employees of the filling station"""

    def __init__(self):
        self.employee_categorry = ['junior pump attendant', 'senior pump attendant', 'station manager']
        self.employee_number = random.randint(0,1000)
        self.employees_file = r'data_files\employees.json'#Employee information is stored in this file
        self.last_generated_emp_number_file = r'data_files\last_generated_number.json'#stores the last generated employee number
        

        
    def create_employee(self,first_name,surname, res_address, phone_number, emp_category):
        """This function is for adding new employees"""
        full_name = first_name + " " + surname
        employee_number = first_name[0:1] + surname + str(self.set_employee_number())
        new_employee_detail = {'employee_number':employee_number, 'first_name':first_name, 'surname':surname,
                               'address':res_address ,'phone_number':phone_number, 'employee_category':emp_category}
        employees__file=[]
        try:
            with open (self.employees_file) as open_file:
                 employees__file = json.load(open_file)#fetch employees informationfor employee in employees_file
                 employees__file.append(new_employee_detail)

        except  json.decoder.JSONDecodeError:
            with open (self.employees_file, 'w') as opened_file:
                json.dump(employees__file,opened_file)
        
        with open (self.employees_file, 'w') as opened_file:
            json.dump(employees__file,opened_file)
             


    def delete_employee(self,employeee_number):
        """This function is for deleting entries for people who are no longer employees"""
        employees_list = []
        with open(self.employees_file, 'r') as file_obj:
            employees_list = json.load(file_obj)#fetch employees information
            for employee in employees_list:
                if employee['employee_number'] == employeee_number:
                    employees_list.remove(employee)
        print('Employee ' + employeee_number + ' has been removed')

        #update employees' file after deleting user
        with open(self.employees_file, 'w') as filename:
            json.dump(employees_list, filename)


    def list_employees(self):
        """lists employees details"""
        print("**************Employees' details****************** ")
        employees_list = []
        try:
            with open(self.employees_file, 'r') as file_obj:
                employees_list = json.load(file_obj)#fetch employees information
                for index, employee in enumerate(employees_list, 1):
                    print('\n'f'{index}: {employee}')
        except  json.decoder.JSONDecodeError:
            print('No employee has been added!')


    

    def get_employee(self,employee_number):
        #lists details about a particular employee#
        employee_detail = {}
        with open(self.employees_file) as file_obj:
            employees_file = json.load(file_obj)#fetch employees informationfor employee in employees_file:
            for employee in employees_file:
                if employee['employeee_number'] == employeee_number:
                    employee_detail = employee

        print( "\n")
        return employee_detail


    def set_employee_number(self):
        """this handles the random generation of employee number"""
        while True:
            employee_number= random.randint(1,10000)
            if employee_number == self.employee_number:
                continue
            else:
                break

        return employee_number


    def get_employee_category(self, employeee_number):
        """returns the employee category"""
        employee_detail = self.get_employee(employeee_number)
        return employee_detail['employee_category']

    def get_employee_detail(self,first_name):
        #lists details about a particular employee#
        employee_detail = {}
        with open(self.employees_file) as file_obj:
            employees_file = json.load(file_obj)#fetch employees informationfor employee in employees_file:
            for employee in employees_file:
                if employee['first_name'] == first_name:
                    employee_detail = employee

        print( "\n")
        if employee_detail:
            return employee_detail
        else:
            return 'Employee not found'
