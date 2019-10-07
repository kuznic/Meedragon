#-------------------------------------------------------------------------------------------------------------#
#                                                                                                             #
#AUTHOR: EMEKA VIN-ANUONYE                                                                                    #
#                                                                                                             #
#This application is a gas station management software                                                        #
#                                                                                                             #
#-------------------------------------------------------------------------------------------------------------#



from login import *
from getpass import getpass
import os



#creates an instance of the login class
my_login = Login()
my_login.employee.create_employee_file()
my_login.filling_station.create_filling_station_file()
my_login.filling_station.pump.create_filling_station_pump_details_file()
my_login.employee.create_last_generated_employee_number_file()





user_name =input('ENTER YOUR USERNAME:')#prompt user to provide user name
passsword = getpass('ENTER YOUR PASSWORD:')#prompt user to enter password

#check to see if user exists
if my_login.employee.verify_user_login(user_name,passsword) == True:

    if my_login.employee.get_employee_category(user_name) == 'station manager' :
        print('Welcome back ' + user_name)
        print("What will you like to do:\n")
        print("\t1.Create an employee")
        print("\t2.View Employees")
        print("\t3.View an Employee")
        print("\t4.Delete an Employee")
        print("\t5.Add a new filling station")
        print("\t6.View filling stations")
        print("\t7.Add pump details for filling station")
        print("\t8.Exit")

        choice= int(input("Please pick an option:"))

        my_login.station_manager_options(choice)


    else : 
        print('Welcome back ' + user_name)
        print("\n")
        print("What will you like to do:\n")
        print("\t1.View your employee details")

        choice= int(input("Please pick an option:"))
        my_login.non_station_manager_options(choice)



#tells the user that username provided does not exist
else:
    print("Invalid login detail provided")



