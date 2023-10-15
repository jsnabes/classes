class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.cargo = False

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True

    def __str__(self):
        return f'{self.make} {self.miles}, {self.price},'

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        self.make = make
        self.miles = miles
        self.price = price
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')

    def __str__(self):
        return f'{self.make} {self.miles}, {self.price} {self.top_speed}'

# Creating lists
bikes = [Motorcycle('Honda', 10000, 5000, 140), Motorcycle('Yamaha', 8000, 6000, 130), Motorcycle('Suzuki', 12000, 5500, 150)]
trucks = [Truck('Ford', 5000, 25000), Truck('Chevrolet', 7000, 27000), Truck('Dodge', 6000, 26000)]
vehicles_to_compare = []

#prompting user to choose category
while True:
    vehicle_type = input('Would you like to view bikes or trucks? Choose 1 for bike or 2 for truck ')

# error message if invalid data selected
    #if vehicle_type != '1' or '2':
        #input('Please choose a valid answer. Choose 1 for bike 2 for truck ')
# if user selects 1 for bikes
    if vehicle_type == '1':
        vehicle_type_list = bikes
        for i in range(len(bikes)):
            print(str(bikes[i]))

# if user selects 2 for trucks
    elif vehicle_type == '2':
        vehicle_type_list = trucks
        for i in range(len(trucks)):
            print(str(trucks[i]))

    # if users wants to compare
    compare = input('Would you like to select a vehicle for comparison? y/n ')

    if compare == 'y':
        vehicle_selection = int(input('Please select which vehicle you would like to add (1, 2 or 3) '))
        chosen_bike = vehicle_type_list[vehicle_selection - 1]
# Need to figure out why getting TypeError
        comparison_vehicle = str(vehicle_type_list.pop(vehicle_selection-1) + vehicle_type_list[vehicle_selection-1].make_noise())
        print(f'{vehicle_type_list[vehicle_selection-1].make} has been added!')
        vehicles_to_compare.append(comparison_vehicle)
        like_to_compare = input('Would you like to compare your vehicles? (y/n) ')
        if like_to_compare == 'y':

            for item in vehicles_to_compare:
                print(str(item, item.make_noise()))
            #item.start_engine)
        #vehicle_type_list[vehicle_selection -1].start_engine
            break

    else:
        break



