"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""
import math

def filter_data(data: dict,min_hight: float, min_weight: float) -> dict:
    """A function that takes a dictionary containing height and weight of students and filters them based on the minimum criteria."""
    return {key: (item[0], item[1]) for key, item in data.items() if math.sqrt((item[0]-min_hight)**2 + (item[1]-min_weight)**2 )<0.5}