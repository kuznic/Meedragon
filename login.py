
from getpass import getpass
from employees import  *
from fillingstation import *
from pump import Pump
class Login():
    """This class handles general administration of the filling station as well as loging into the application"""

    def __init__(self):
        self.employee = Employees()
        self.filling_station = FillingStation('Initalized','Initalized')
        self.pump = Pump()
        self.login_users_file = r'data_files\users.json'
        self.user_role = ['admin', 'non-admin']
    
    def create_user(self,user, passwrd):
        """This creates a new user login credential"""
        file = []
        with open (self.login_users_file, 'r') as fobj:
                file = json.load(fobj)
        
        passwrd_hash = self.hash_password(passwrd)
        user_login_role = ''
        choice = 1
        print("Choose User role from the list below:")
        for role in sorted(self.user_role):
            print("\t" + str(choice) +'.' + role)
            choice=choice + 1
        userr_role = int(input("ROLE: "))
        if userr_role==1:
            user_login_role = "admin"
        elif userr_role==2:
            user_login_role= 'non-admin'

        new_user = {'user_name':user, 'password':passwrd_hash, 'role':user_login_role}
        file.append(new_user)
        with open(self.login_users_file, 'w') as f:
            json.dump(file,f)

    def get_user(self,user_name):
        """fetchs a user login detail"""
        user_detail = {}
        with open(self.login_users_file) as file_obj:
            users_file = json.load(file_obj)#fetch user login information:
            for user in users_file:
                if user['user_name'] == user_name:
                    user_detail = user
        return user_detail


    def hash_password(self,password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self,stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',provided_password.encode('utf-8'), salt.encode('ascii'),100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def verify_user_login(self, user_name, password):
        """Verify user login credentials"""
        try:
            login_detail = self.get_user(user_name)
            hashed_pword = login_detail['password']
            if login_detail:
                if self.verify_password(hashed_pword,password) == True:
                    return True
                else:
                    return False
            else:
                return False
           
            #If user doesn't exist then this is triggered
        except KeyError:
            return False
    
    def station_manager_options(self,choice):

        """Handles the different administrative functions a station manager can perform"""
        #create employee
        if choice ==1:
            firstname=input("Enter the firstname of the employee: ")
            lastname=input("Enter the lastname of the employee: ")
            res_address=input("Enter the residential address of the employee: ")
            phone_number=input("Enter the phone number of the employee: ")
            employee_category = ''
            print("Choose employee category from the list below:")
            for category in sorted(self.employee.employee_categorry):
                print("\t" + str(choice) +'.' + category)
                choice=choice + 1#using this to assign numbers to the line above
            employee_category_choice = int(input("Category? "))
            if employee_category_choice==1:
                employee_category = "junior pump attendant"
            elif employee_category_choice==2:
                employee_category = 'senior pump attendant'
            elif employee_category_choice==3:
                employee_category = 'station manager'

            self.employee.create_employee(firstname, lastname, res_address,phone_number,employee_category)
            print("New employee has been created successfully!")
       
        #view employees' details
        elif choice ==2:
            self.employee.list_employees()

        #view employee detail
        elif choice ==3:
            firsst_name=input("Enter the first name of the employee: ")
            emp_detail=self.employee.get_employee_detail(firsst_name)
            print(emp_detail)

        #delete an employee
        elif choice ==4:
            usr_name=input("Enter the username of the user to be deleted:")
            self.employee.delete_employee(usr_name)

        #add new filling station
        elif choice ==5:
            name_of_filling_station = input('Enter the name of the filling station:')
            location_of_filling_station = input('Enter the address of the filling station:')
            number_of_pumps = int(input ('Enter the number of pumps:'))
            
            self.filling_station.create_filling_station(name_of_filling_station,location_of_filling_station,number_of_pumps)
      
                
        
        #view filling stations details
        elif choice ==6:
           self.filling_station.list_stations()

        #Add pump details for filling station
        elif choice ==7:
            name_of_filling_station = input('Enter the name of the filling station:')
            if self.filling_station.get_station(name_of_filling_station):#check that filling sation exists
                counter = int(self.filling_station.get_station(name_of_filling_station)['number_of_pumps'])#fetch number of pumps

                while True:
                    if counter >= 1:
                        pump_manufacturer = input("Enter the name of the manufacturer of pump " + str(counter) +":")
                        manufacture_date = input("Enter the date of manufacture of pump " + str(counter)+":")
                        type_of_pump = input("Enter the type of pump of pump " + str(counter) +":")
                        self.pump.set_type_of_pump(type_of_pump)
                        pump_capacity = int(input("Enter the pump capacity  of pump " + str(counter) + ":"))

                        self.pump.add_filling_station_pump_details(name_of_filling_station,counter,pump_manufacturer,
                                                                        manufacture_date,type_of_pump,pump_capacity)
                        counter-=1
       
               
                    else:
                        break

            else:
                print("This filling station " + name_of_filling_station + " does not exist!")

         #create new user
        elif choice ==8:
            username=input('ENTER USERNAME:')
            passwod=getpass('ENTER PASSWORD:')
            self.create_user(username,passwod)
             

        #Exit program
        elif choice == 9:
            print('Exiting Program........')
            print('Program exited!')
            pass
        
      
    def non_station_manager_options(self, choice):
        """Handles the different administrative functions a non-station manager can perform"""
        if choice ==1:
            emp_detail=self.employee.list_employees()
            print(emp_detail)

