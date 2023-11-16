import math

def find_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ask the user for two sets of x,y coordinates
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the distance between the two points
distance = find_distance(x1, y1, x2, y2)

# Print the distance
print(f"The distance between the two points is: {distance}")