import json
from login import Login
from getpass import getpass
class CreateJsonDataFiles():
    """This class handles the creation as well as the intialization where required of 
    the json data files used for this application"""

    def __init__(self):
       self.employees_file = r'data_files\employees.json'#Employee information is stored in this file
       self.last_generated_emp_number_file = r'data_files\last_generated_number.json'#stores the last generated employee number
       self.login_users_file = r'data_files\users.json'
       self.filling_station_file = r'data_files\filling_station.json'#Filling station information is stored in this file
       self.filling_station_pump_file = r'data_files\filling_station_pump_details.json'#Filling station pump details information is stored in this file
       self.login = Login()


    def create_login_users_file(self):
        """This function creates the users file that hold the login credentials 
        of users of the application and prompts to create a default user"""
        try:
            with open (self.login_users_file, 'r') as fobj:
                file = json.load(fobj)

        except FileNotFoundError:
            print('Create a default user for the application')
            default_username=input('Enter the default username:')
            passwod=getpass('Enter the default password:')
            print('\n')
            hashed_paswod = self.login.hash_password(passwod)

            default_user = [{'user_name':default_username,'password':hashed_paswod, 'role':'admin'}]

            with open(self.login_users_file, 'w') as fl:
                json.dump(default_user,fl)



    def create_employee_file(self):
        """This function creates the employees file"""
        open(self.employees_file , 'a').close()
        


    def create_last_generated_employee_number_file(self):
        """This creates the file that holds information about the last generated employee number"""
        open(self.last_generated_emp_number_file, 'a') .close()
                
    def create_filling_station_file(self):
        """This creates a json file that holds information about the filling station"""
        open(self.filling_station_file, 'a').close()

    def create_filling_station_pump_details_file(self):
        """This creates a json file that holds information about the filling station pumps"""
        open(self.filling_station_pump_file, 'a').close()

#'1a36c6b67d1d15ef6ca2819582bcb7b82fe487725072ee939f00a26b94318b7322e473deaa93ca9e2a08346ee1aeff564635e5f5e5b7d3db142274a24a621e2377b06b18bfcc238760f0c8ff9ccf2f46a628def9fd2503f2a2a0d45685c941bd'}]=
