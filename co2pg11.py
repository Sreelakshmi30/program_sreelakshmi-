#write lambda function to find area of square,rectangle and triangle#

import math
rect_area=lambda l,b:l*b
triangle_area=lambda b,h:(b*h)/2
square_area=lambda a:a*a
print("area of rectangle(10,20) is:",rect_area(10,20))
print("area of triangle(10,20) is:",triangle_area(10,20))
print("area of square(10) is:",square_area(10))
