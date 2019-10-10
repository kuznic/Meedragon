import os, json

"""This module models a typical gas filling station """
class FillingStation():
    """ This class defines the general information about the filling station"""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.filling_station_file = r'data_files\filling_station.json'#Petrol station information is stored in this file

    def get_filling_station_profile(self):
        """provides a summary of the filling station"""
        print("\nProfile of " + self.name.title() + " filling station:")
        print("NAME:" + self.name)
        print("ADDRESS:" + self.location)
        print("TOTAL NUMBER OF PUMPS:" + str(self.pump.get_number_of_pumps()))

    

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
            

