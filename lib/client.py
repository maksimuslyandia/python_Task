from lib.system import System


class Client:
    rent_types_dict = {
        "1": "hour",
        "2": "day",
        "3": "week"
    }

    def __init__(self):
        self.system = System
        # Initiates a list of all the cars
        self.system.start()

    def list_cars(self):
        self.system.display_available_cars()

    def choose(self):
        """Based on the number of cars that the client object is going to rent,
        this method calculates the total price of the order.

        Returns:
            float: The cost of your order.
        """
        total_price = 0
        license_plates = None

        num_cars = self._get_number_of_cars_to_rent()
        
        # Using an underscore (_) because we are not going to use the indexes
        # of this loop, this is a convention.
        for _ in range(num_cars):
            license_plate, current_price = self._single_choice()
            total_price += current_price
            print(f"Successfully rented car with a license plate |{license_plate}| for ${current_price}")

        # 30% discount
        if num_cars >= 3:
            return total_price - total_price * 0.3

        return total_price

    def _get_number_of_cars_to_rent(self):

        while True:
            num_cars = input("Enter the number of cars that you are going to rent: ")
            
            if int(num_cars) >= 1:
                return int(num_cars)


    def _single_choice(self):
        """Pipeline of loops for the rent of a single car.

        Returns:
            tuple: The chosen license plate and the cost of its rental.
        """
        chosen_license_plate = self._get_license_plate()
        
        rent_type = self._get_rent_type()
        factor = self._get_rent_factor(rent_type)
        
        rent_cost = self.system.rent(
            chosen_license_plate, self.rent_types_dict[rent_type], factor
        )

        return chosen_license_plate, rent_cost

    def _get_rent_factor(self, rent_type):
        """Validates and returns the factor, that is going to be multiplied with
        the price of a single vehicle. 
        E.g - if we want to rent a car for 5 hours and its price for 1 hour is $10
        the result will be - factor * $10, where factor = 5. 

        Args:
            rent_type (string): Either '1', '2' or '3', for 'hour', 'day', 'week'

        Returns:
            int: Integer representing the factor.
        """

        while True:
            factor = input(f"Enter the number of {self.rent_types_dict[rent_type].upper()}S for which you are going to rent the vehicle: ")
            
            if int(factor) >= 1:
                return int(factor)
            
            else:
                print("The rent factor can't be less than 1!")

    def _get_license_plate(self):
        """Validates if the license plate exists and then returns it.
        If it does not exist, the loop continues to ask the Client to enter  
        another license plate.

        Returns:
            string: License plate value.
        """
        available_license_plates = self.system.get_license_plates()

        while True:
            chosen_license_plate = input("Enter car license plate: ")
            
            if chosen_license_plate in available_license_plates:
                return chosen_license_plate
            
            else:
                print("This license plate does NOT exist, try with another one!")

    def _get_rent_type(self):
        """Asks the Client to enter a rent type. If the entered rent type is 
        not a valid one, the Client continues being asked.

        Returns:
            string: Either '1', '2' or '3', for 'hour', 'day', 'week'
        """
        type_is_valid = False
        
        while not type_is_valid:
            print("-" * 35)
            print("1 - For hour/s\n2 - For day/s\n3 - For week/s")
            rent_type = input("Enter a number representing the type of the rent: ")
            # Validating whether the rent type exists or not
            type_is_valid = self._rent_type_is_valid(rent_type)
            
            if not type_is_valid:
                print("You have to enter either 1, 2 or 3 for your rent types!")
            print("-" * 35)

        return rent_type

    def _rent_type_is_valid(self, chosen_type):
        
        if chosen_type in self.rent_types_dict.keys():
            return True

        return False