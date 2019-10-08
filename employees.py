import json,random,hashlib, binascii, os
from salary import Salary
class Employees():
    """This class details information about the employees of the filling station"""

    def __init__(self):
        self.employee_categorry = ['junior pump attendant', 'senior pump attendant', 'station manager']
        self.employees_file = r'data_files\employees.json'#Employee information is stored in this file
        self.last_generated_emp_number_file = r'data_files\last_generated_number.json'
        self.employee_number = random.randint(0,1000)
        self.emp_salary = Salary()#creates instance of the Salry class as an attribute of the Employee class
       
    def create_employee_file(self):
        """This function creates the employees file and adds a default user"""
        try:
            with open(self.employees_file, 'r') as fil_obj:
                file = json.load(fil_obj)
        except FileNotFoundError:
            hashed_password = self.hash_password('admin')
            default_user = [{'user_name':'admin','first_name':'admin','password':hashed_password,
                             'employee_category':'station manager'}]
            with open(self.employees_file, 'w') as file:
                json.dump(default_user, file)

        except  json.decoder.JSONDecodeError:
            hashed_password = self.hash_password('admin')
            default_user = [{'user_name':'admin','password':hashed_password,'employee_category':'station manager'}]
            with open(self.employees_file, 'w') as file:
                json.dump(default_user, file)


    def create_last_generated_employee_number_file(self):
        """This creates the file that holds information about the last generated employee number"""
        try:
            with open(self.last_generated_emp_number_file, 'r') as file_object:
                self.employee_number = json.load(file_object)
                print(self.employee_number)
        except FileNotFoundError:
            with open(self.last_generated_emp_number_file, 'w') as file:
                json.dump(self.employee_number, file)

        except json.decoder.JSONDecodeError:
            with open(self.last_generated_emp_number_file, 'w') as file:
                json.dump(self.employee_number, file)

        
    def create_employee(self,first_name,surname, res_address, phone_number, emp_category,password):
        """This function is for adding new employees"""
        full_name = first_name + " " + surname
        user_name = first_name[0:1] + surname
        employee_number = first_name[0:1] + surname + str(self.set_employee_number())
        hashed_password = self.hash_password(password)
        new_employee_detail = {'user_name': user_name,'password':hashed_password,'employee_number':employee_number, 'first_name':first_name, 
                               'surname':surname,'address':res_address ,'phone_number':phone_number, 'employee_category':emp_category}
        employees__file=[]
        with open (self.employees_file) as open_file:
             employees__file = json.load(open_file)#fetch employees informationfor employee in employees_file
             employees__file.append(new_employee_detail)
        
        with open (self.employees_file, 'w') as opened_file:
            json.dump(employees__file,opened_file)
             


    def delete_employee(self,user_name):
        """This function is for deleting users who are no longer employees"""
        employees_list = []
        with open(self.employees_file, 'r') as file_obj:
            employees_list = json.load(file_obj)#fetch employees information
            for employee in employees_list:
                if employee['user_name'] == user_name:
                    employees_list.remove(employee)
        print('Employee ' + user_name + ' has been removed')

        #update employees' file after deleting user
        with open(self.employees_file, 'w') as filename:
            json.dump(employees_list, filename)


    def list_employees(self):
        """lists employees details"""
        print("Employees' details: ")
        employees_list = []
        with open(self.employees_file, 'r') as file_obj:
            employees_list = json.load(file_obj)#fetch employees information
            for employee in employees_list:
                print(employee)


    

    def get_employee(self,user_name):
        #lists details about a particular employee#
        employee_detail = {}
        with open(self.employees_file) as file_obj:
            employees_file = json.load(file_obj)#fetch employees informationfor employee in employees_file:
            for employee in employees_file:
                if employee['user_name'] == user_name:
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


    def get_employee_category(self, usr_name):
        """returns the employee category"""
        employee_detail = self.get_employee(usr_name)
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
