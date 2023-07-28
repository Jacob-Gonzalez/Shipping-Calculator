# Project Name:  Shipping-Calculator
# Discription:   Build a program that will calculate the shipping cost for all shipping methods based on the package weight. 
#                Project was provided by Codecademy to test knowledge on basic fundamentals of conditional statements.
# Author:        Jacob Gonzalez (28 July 2023)  

weight = float(input("Please enter the weight of your package in pounds:  "))
ground_shipping_rate = 20.00
ground_shipping_premium_rate = 125.00
drone_shipping_rate = 0.00

# create if/elif/else statement to calculate ground shipping based on the given weight
if weight <= 2.0:
    ground_shipping_rate += (weight * 1.50)
    print("Total cost for ground shipping:  $%.2f" % ground_shipping_rate, "\nStandard delivery (3-5 days)\n")
elif weight <= 6.0:
    ground_shipping_rate += (weight * 3.00)
    print("Total cost for ground shipping:  $%.2f" % ground_shipping_rate, "\nStandard delivery (3-5 days)\n")
elif weight <= 10.0:
    ground_shipping_rate += (weight * 4.00)
    print("Total cost for ground shipping:  $%.2f" % ground_shipping_rate, "\nStandard delivery (3-5 days)\n")
else: 
    ground_shipping_rate += (weight * 4.75)
    print("Total cost for ground shipping:  $%.2f" % ground_shipping_rate, "\nStandard delivery (3-5 days)\n")

# ground shipping premium has a much higher rate and does not charge per pound
print("Total cost for ground shipping premium:  $%.2f" % ground_shipping_premium_rate, "\nExpedited delivery (1-3 days)\n")

# create if/elif/else statement to calculate drone shipping based on the given weight
if weight <= 2.0:
    drone_shipping_rate += (weight * 4.50)
    print("Total cost for drone shipping:  $%.2f" % drone_shipping_rate, "\nSame day delivery\n")
elif weight <= 6.0:
    drone_shipping_rate += (weight * 9.00)
    print("Total cost for drone shipping:  $%.2f" % drone_shipping_rate, "\nSame day delivery\n")
elif weight <= 10.0:
    drone_shipping_rate += (weight * 12.00)
    print("Total cost for drone shipping:  $%.2f" % drone_shipping_rate, "\nSame day delivery\n")
else: 
    drone_shipping_rate += (weight * 14.25)
    print("Total cost for drone shipping:  $%.2f" % drone_shipping_rate, "\nSame day delivery\n")