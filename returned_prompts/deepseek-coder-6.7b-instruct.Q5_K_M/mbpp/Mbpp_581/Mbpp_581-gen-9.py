import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

print(distance((1,2), (4,6)) == 5.0)

"""
Write a python function to find the perimeter of