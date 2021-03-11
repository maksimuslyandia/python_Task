#!C:\Users\maksimuslyandia\AppData\Local\Programs\Python\Python39\python.exe
# print("Content-Type: text/html")

import json
import sys


class CarStore(object):
  
  def __init__(self):
    
    try:
      with open('cars_list.json') as json_file:
        self.cars_list = json.load(json_file)
        
    except IOError:
      self.datadata ={}
      print("Error: File does not exist. Please, create file first")
      sys.exit()

  def get_cars(self):
    return self.cars_list
    
      # for params in car:
      #   print(params)
  def get_car_by_id(self,car_id):
       
    for car in self.cars_list['cars']:
      if(car_id==car['car_id']):
        return car
    


    return self.cars_list
    
      # for params in car:
      #   print(params)

  def getCarsList(self):
    print('Please, choose car that you want to drive next:')
    x = int(input("Enter a car number: "))
    print(x)

class Client(CarStore):
  
  def __init__(self):
    self.CarStore=CarStore()
    self.seleced_cars = []
    
    
  def select_car(self):
    print("Please choose car")
    self.cars_list = self.CarStore.get_cars()
    for car in self.cars_list['cars']:
        print(str(car["car_id"])+ ". "+ car["car_brand"]+" "+car["model"])
    while True:
      try:
        self.userInput = int(input())       
      except ValueError:
        print("Not an integer! Try again.")
        continue
      else:
        self.seleced_cars.append(self.userInput)
        print("your choice is " + self.cars_list['cars'][self.userInput]["car_brand"]+" "+self.cars_list['cars'][self.userInput]["model"])
        break     

  def select_how_long(self):
    during_time = ["hours","days", "weeks"]
    during = ["Price_per_hour","Price_per_day", "Price_per_week"]
    
    print("Select how long time do you want to rent a car")
    print("0. in hours")
    print("1. in days")
    print("2. in weeks")
    while True:
      try:
        how_long = int(input())
      except ValueError: 
        print("Not an integer! Try again.")
        continue
      else:
        break
    print("How many/much " + during_time[how_long]+" do you want to rent ")
    self.during_time = during[how_long]
    while True:
      try:
        self.how_mach = int(input())
      except ValueError: 
        print("Not an integer! Try again."+str(self.how_mach))
        continue
      else:
        break
    # print("how many/much " + during[how_long] + "do you wand to rent?")
    
    #  while True:
    #   try:
    #     how_long = int(input())
    #   except ValueError: 
    #     print("Not an integer! Try again.")
    #     continue
    #   else:
    #     print("you are selected " + during[how_long])
    #     break  

  def calculate_price(self):
    Car = CarStore()
    selected_car = Car.get_car_by_id(2)
    print("Total price is " + str(int(selected_car[self.during_time])* self.how_mach))
    return 
    
    
  def check_int(self,var_to_check):
    try:
      return int(var_to_check)
    except IOError:
      print('Please, choose ')



Client = Client()
Client.select_car()
Client.select_how_long()
#TODO ask question and do again
Client.calculate_price() 
