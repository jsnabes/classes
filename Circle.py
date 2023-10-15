import math

# Creating class
class Circle:
    def __int__(self, radius, diam, circum, area):
        self.radius = radius
        self.diam = diam
        self.circum = circum
        self.area = area

# Trying to create objects of Circle class to add to __str__
#diam = Circle()
#circum = Circle()
#area = Circle()

# add methods here
    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return 2 * math.pi * self.radius ** 2

    def grow(self):
        return 2 * self.radius

    def get_radius(self):
        return self.radius

    def __str__(self):
        return f"Diameter: {self.diam} \nCircumference: {self.circum} \nArea: {self.area}"

#Tried calling functions to see if that helped with __str__
#calculate_diameter = ()
#calculate_circumference = ()
#calculate_area = ()


# start of program and getting user input
input_radius = None

prompt = input("Please enter a radius: ")

# Returning dimensions based on radius. Doesn't need to be in a loop- only going
# through once
print(str(Circle.calculate_diameter))
print(str(Circle.calculate_circumference))
print(str(Circle.calculate_area))

ask_grow = input("Would you like your circle to grow? (y/n) ")
if ask_grow == 'y':
    print("Stand by while your circle magically grows...")
    print(f"{Circle.grow}")
else:
    print("Goodbye")

