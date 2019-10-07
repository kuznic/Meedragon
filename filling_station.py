import os, json

"""This module models a typical gas filling station """
class StationProfile():
    """ This class defines the general information about the filling station"""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.pump = Pump()
        self.filling_station_file = r'data_files\filling_station.json'#Petrol station information is stored in this file

    def get_filling_station_profile(self):
        """provides a summary of the filling station"""
        print("\nProfile of " + self.name.title() + " filling station:")
        print("NAME:" + self.name)
        print("ADDRESS:" + self.location)
        print("TOTAL NUMBER OF PUMPS:" + str(self.pump.get_number_of_pumps()))

    def create_filling_station_file(self):
        """This creates a json file that holds information about the petrol station"""
        try:
            with open(self.filling_station_file, 'r') as fil_obj:
                file = json.load(fil_obj)
        except FileNotFoundError:
            open(r'data_files\filling_station.json','a')

        except  json.decoder.JSONDecodeError:
           pass

    def create_filling_station(self,name_of_station,address, number_of_pumps):
        """This function adds new petrol stations to the petrol_station json file"""
        new_station_detail = {'station_name': name_of_station,'address':address, 
                              'number_of_pumps':number_of_pumps}
        station_file=[]
        try:
            with open (self.filling_station_file) as open_file:
                 station_file = json.load(open_file)#load station file
                 station_file.append(new_station_detail)

        except  json.decoder.JSONDecodeError:
            station_file.append(new_station_detail)
            with open (self.filling_station_file, 'w') as opened_file:
                json.dump(station_file,opened_file)

        with open (self.filling_station_file, 'w') as opened_file:
                json.dump(station_file,opened_file)

    def list_stations(self):
        """lists stations' details"""
        print("Stations' details: ")
        stations_list = []
        with open(self.filling_station_file, 'r') as file_obj:
            stations_list = json.load(file_obj)#fetch stations' information
            for station in stations_list:
                print(station)

    def get_station(self,station_name):
            """fetch detail about a particular filling station"""
            station_detail = {}
            try:
                with open(self.filling_station_file) as file_obj:
                    stations_file = json.load(file_obj)#fetch filling stations information for station in stations_file:
                    for station in stations_file:
                        if station['station_name'] == station_name:
                            station_detail = station
            
            except json.decoder.JSONDecodeError:
                pass

            return station_detail
            


class Pump():
    """This class provides information about the pumps present in the filling station. 
    Pump() class has the following attributes which have been initialized with default values:
    i.) manufacturer
    ii.)date of manufacture
    iii.)type of pump
    iv.)number of pumps"""

    def __init__(self):
        self.manufacturer= ''
        self.date_of_manufacture= ''
        self.type_of_pump = ''
        self.number_of_pumps = 0
        self.pump_capacity = 0
        self.filling_station_pump_file = r'data_files\filling_station_pump_details.json'#Petrol station pump details information is stored in this file
        self.pump_level = 0
    def create_filling_station_pump_details_file(self):
        """This creates a json file that holds information about the petrol station pumps"""
        try:
            with open(self.filling_station_pump_file, 'r') as fil_obj:
                file = json.load(fil_obj)
        except FileNotFoundError:
            open(r'data_files\filling_station_pump_details.json','a')

        except  json.decoder.JSONDecodeError:
           pass

    def set_pump_manufacturer(self, manufacturer):
        """ sets the pump manufacturer"""
        self.manufacturer = manufacturer
        
    def get_pump_manufacturer(self):
        """fetches the name of the manufacturer"""
        return self.manufacturer

    def set_date_of_manufacture(self,date_of_manufacture):
        """sets the date of manufacture of the pump"""
        self.date_of_manufacture = date_of_manufacture

    def get_date_of_manufacture(self):
        """fetches date of manufacture"""
        return self.date_of_manufacture
            
    def set_type_of_pump(self,type_of_pump):
        """sets the type of pump"""
        self.type_of_pump = type_of_pump

    def get_type_of_pump(self):
        """fetches the type of pump"""
        return self.type_of_pump

    def set_number_of_pumps(self,number_of_pumps):
        """sets the number of pumps"""
        self.number_of_pumps = number_of_pumps

    def get_number_of_pumps(self):
        """fetches the number of pumps"""
        return self.number_of_pumps

    def set_pump_capacity(self,pump_capacity):
        """sets the capacity of the pump"""
        self.pump_capacity=pump_capacity

    def get_pump_capacity(self):
        """fetches the capacity of the pump"""
        return self.pump_capacity

    def add_filling_station_pump_details(self,station_name,pump_number,pump_manufacturer,date_of_manufacture,type_of_pump,pump_capacity):
        """This function adds new filling station pump details  to the filling_station pump details json file"""
        new_station_pump_detail = {'station_name': station_name,'pump_number':pump_number,'pump_manufacturer':pump_manufacturer,
                                   'date_of_manufacture':date_of_manufacture,'type_of_pump':type_of_pump,
                                   'pump_capacity':pump_capacity, 'gas_level':self.pump_level}
        pump_details_file=[]
        try:
            with open (self.filling_station_pump_file) as open_file:
                 pump_details_file = json.load(open_file)#load station file
                 pump_details_file.append(new_station_pump_detail)

        except  json.decoder.JSONDecodeError:
            pump_details_file.append(new_station_pump_detail)
            with open (self.filling_station_pump_file, 'w') as opened_file:
                json.dump(pump_details_file,opened_file)

        with open (self.filling_station_pump_file, 'w') as opened_file:
                json.dump(pump_details_file,opened_file)
                

