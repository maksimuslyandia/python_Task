from lib.car_factory import CarFactory


class System:

    @classmethod
    def start(cls):
        cls.all_cars = CarFactory.get_cars()

    @classmethod
    def rent(cls, license_plate, rent_type, factor):
        """Calculates the price of a car rental.

        Args:
            license_plate (string): The license plate string.
            rent_type (string): Either 'hour', 'day' or 'week'.
            factor (int): Factor by which the cost is multiplied.

        Returns:
            float: The result of the multiplication of the factor and the 
            rent cost for the chosen car.
        """
        
        for car in cls.all_cars:
            
            if not car.is_rented and car.license_plate == license_plate:
                rent_cost = car.calculate_rent(rent_type)
                
                return factor * rent_cost
        
        return None

    @classmethod
    def display_available_cars(cls):
        available_cars = 0
        print("-" * 38)
        print("-" * 12 + "AVAILABLE CARS" + "-" * 12)
        print("-" * 38)
        
        for car in cls.all_cars:
            
            if not car.is_rented:
                available_cars += 1
                print(str(car))
        
        print(f"Available Cars: {available_cars}")
        print("-" * 38)

    @classmethod
    def get_license_plates(cls):
        license_plates = []

        for car in cls.all_cars:
            
            if not car.is_rented:
                license_plates.append(car.license_plate)

        return license_plates
    