import json
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
                


