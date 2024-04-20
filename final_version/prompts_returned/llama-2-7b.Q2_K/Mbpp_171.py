"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
import math

def perimeter_pentagon(sides):
    pentagon = []
    for i in range (0, sides+1,5):
        if not (math.isnan(i) or math.isinf(i)):
            pentagon.append((i))
    return sum(x for x in pentagon[2:] if x-1 >= 0 and x+1 <= sides) + sum(x in pentagon[:2] for x in pentagon[3:])
"""Write a function to find the perimeter of an irregular polygon. If it is given as an array, this is very simple; otherwise you must write your own version of the function below."""
def perimeter_polygon(sides):
    polygon = []
    for i in range (0, sides+1,5):
        if not (math.isnan(i) or math.isinf(i)):
            polygon.append((i))
            
    polygon.sort()
    return sum(x in polygon[2:] for x in polygon[:] if x-1 >= 0 and x+1 <= sides) + sum(x in polygon[:2] for x in polygon[3:])