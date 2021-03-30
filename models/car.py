import json


class Car:

    def __init__(self, brand, model, license_plate, 
                 hour_rent, day_rent, week_rent, consumption):
        self._brand = brand
        self._model = model
        self._consumption = consumption
        self._license_plate = license_plate
        self._hour_rent = hour_rent
        self._day_rent = day_rent
        self._week_rent = week_rent
        self._is_rented = False

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self):
        print("You are not allowed to change the license plate from here.")

    @property
    def is_rented(self):
        return self._is_rented

    @is_rented.setter
    def is_rented(self, new_is_rented_flag):
        
        # Using a setter for encapsulation & safety measures,
        # because the _is_rented flag is going to be used from outer modules.
        if new_is_rented_flag == True or new_is_rented_flag == False:
            self._is_rented = new_is_rented_flag
    
    def rent(self, type_="hour"):
        
        if not self._is_rented:
            price = self.calculate_rent(type_)
        
        else:
            print("This car is currently rented")

    def calculate_rent(self, type_):
        rent_cost = getattr(self, f"_{type_}_rent")
        self._is_rented = True

        return rent_cost

    def __str__(self):
        """Dunder method for easier printing of the car as a string.
        E.g. if the __str__() method is implemented, we can print
        a Car object as str(car_object), with a format that we've chosen.

        Returns:
            string: The chosen format of a descriptive object string.
        """
        border = '-' * 30
        header = f"{self._brand.capitalize()} - {self._model}"
        info = f"Renting Prices:\nHour: ${self._hour_rent}, Day: ${self._day_rent}, Week: ${self._week_rent}"
        license_plate_info = f"License plate: {self.license_plate}"

        return f"{border}\n{header}\n{info}\n{license_plate_info}\n{border}"

    