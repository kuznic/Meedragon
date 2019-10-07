from employees import  *
from filling_station import *
class Login():
    """This class handles general administration of the filling station as well as loging into the application"""

    def __init__(self):
        self.employee = Employees()
        self.filling_station = StationProfile('Initalized','Initalized')


    def station_manager_options(self,choice):

        """Handles the different administrative functions a station manager can perform"""
        #create employee
        if choice ==1:
            firstname=input("Enter the firstname of the employee: ")
            lastname=input("Enter the lastname of the employee: ")
            res_address=input("Enter the residential address of the employee: ")
            phone_number=input("Enter the phone number of the employee: ")
            password = input("Enter password for the new employee:")
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

            self.employee.create_employee(firstname, lastname, res_address,phone_number,employee_category,password)
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
                        self.filling_station.pump.set_type_of_pump(type_of_pump)
                        pump_capacity = int(input("Enter the pump capacity  of pump " + str(counter) + ":"))

                        self.filling_station.pump.add_filling_station_pump_details(name_of_filling_station,counter,pump_manufacturer,
                                                                        manufacture_date,type_of_pump,pump_capacity)
                        counter-=1
       
               
                    else:
                        break

            else:
                print("This filling station " + name_of_filling_station + " does not exist!")


        #Exit program
        elif choice == 8:
            print('Exiting Program........')
            print('Program exited!')
            pass
        
      
    def non_station_manager_options(self, choice):
        """Handles the different administrative functions a non-station manager can perform"""
        if choice ==1:
            emp_detail=self.employee.get_employee(user_name)
            print(emp_detail)



