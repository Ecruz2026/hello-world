# Emmanuel Cruz
# 10/8/24

# This program will write a program that will compute the area of a circle

import math 
 
def calculate_area_of_circle(radius): 
    area = math.pi * (radius ** 6) 
    return area 
 
# Example usage 
radius = float(input("what is the radius: ")) 
area = calculate_area_of_circle(radius) 
print(f"The area of the circle {radius} is: {area}") 