import unittest
import json
from employees import *

class Test_test_employee(unittest.TestCase):
    """Test for employees class"""

    def setUp(self):
        self.test_employees = Employees()#creates an instance of the Employees class
        self.test_employees.employees_file = 'test_employees.json'
        self.employee_detail = {'first_name':'Emeka', 'last_name':'Vin',
                                'res_add':'Lagos','phone_num':'042342343',
                                'category':'station manager'}
        self.created = {'user_name': 'EVin', 'first_name': 'Emeka','surname': 'Vin',
                         'address': 'Lagos', 'phone_number': '042342343', 'employee_category': 'station manager'}
        self.emp_file = []
       


    def test_create_employee(self):
        """test the create_employee function. This tests that employee is successfully created"""
        try:
            with open(self.test_employees.employees_file, 'r') as file_obj:
                self.emp_file=json.load(file_obj)
        except FileNotFoundError:
            default_user = [{'user_name':'admin','employee_category':'station manager'}]
            with open(self.test_employees.employees_file, 'w') as file:
                json.dump(default_user, file)
        self.test_employees.create_employee(self.employee_detail['first_name'],self.employee_detail['last_name'],
                                            self.employee_detail['res_add'],self.employee_detail['phone_num'],
                                            self.employee_detail['category'])
        with open(self.test_employees.employees_file, 'r') as f_obj:
            self.emp_file = json.load(f_obj)
        self.assertIn(self.created,self.emp_file)



unittest.main()
