import json

from models.car import Car
from config import STORAGE_PATH


class CarFactory:
    
    @classmethod
    def get_cars(cls):
        cls._read_storage()
        cls._create_cars_list()
        
        return cls.cars

    @classmethod
    def _read_storage(cls):

        with open(STORAGE_PATH) as json_file:
            data = json_file.read()
            # Implicitly creating the storage (class attribute)
            cls.storage = json.loads(data)

        # Returing it for safer usage
        return cls.storage

    @classmethod
    def _create_cars_list(cls):
        cars_jsons_list = cls.storage["cars"]
        cls.cars = []

        for car_params in cars_jsons_list:
            cls.cars.append(Car(**car_params))

        return cls.cars
