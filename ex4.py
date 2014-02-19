# Variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 

# Calculate 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# If you get this error shown bellow: 
#==================================================================
# Traceback (most recent call last):
#   File "ex4.py", line 15, in <module>
#     print "We can transport", carpool_capacity, "people today."
# NameError: name 'car_pool_capacity' is not defined
#==================================================================
# The answer is logical. It says it's a "NameError, and in this case the name "carpool_capacity" was written as "car_pool_capacity. 
# Due to the difference between the two words, neither of them an be defined or get a value
