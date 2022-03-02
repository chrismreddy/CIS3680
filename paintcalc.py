import math

SQFT_PER_DOOR = 14.0
SQFT_PER_WINDOW = 8.5
SQFT_PER_GALLON = 350.0

wall_length = float(input("Enter wall length (ft): "))
wall_height = float(input("Enter wall height (ft): "))
wall_area = wall_height * wall_length

door_count = int(input("Enter number of doors: "))
door_allowance = door_count * SQFT_PER_DOOR

window_count = int(input("Enter number of windows: "))
window_allowance = window_count * SQFT_PER_WINDOW

total_area = wall_area - door_allowance - window_allowance

gallons = total_area / SQFT_PER_GALLON
gallons = math.ceil(gallons)

paint_price = float(input("Enter the price of selected paint: "))
cost = gallons * paint_price

print("Gallons needed:", gallons)
print("Paint Cost: {0:.2f}".format(cost))