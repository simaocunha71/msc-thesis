def count_charac(string):
    total_length = 0
    for i in string:
        total_length += 1
    return total_length

def test_count_charac():
    assert count_charac("python programming") == 18

test_count_charac()



"""
Write a function that will return the sum of all the elements in a list.

assert sum_list([1, 2, 3, 4])==10
"""

def sum_list(list_num):
    total_sum = 0
    for i in range(len(list_num)):
        total_sum += list_num[i]
    return total_sum

def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10

test_sum_list()


"""
Write a function to calculate the area of a circle.

assert calculate_area(10)==314.1592653589793
"""
def calculate_area(radius):
    area = (22 / 7) * radius * radius
    return area

def test_calculate_area():
    assert calculate_area(10) == 314.1592653589793

test_calculate_area()


"""
Write a function to calculate the area of a rectangle.

assert calculate_rectangle_area(8, 10)==80
"""

def calculate_rectangle_area(length, breadth):
    area = length * breadth
    return area

def test_calculate_rectangle_area():
    assert calculate_rectangle_area(8, 10) == 80

test_calculate_rectangle_area()


"""
Write a function to calculate the area of a triangle.

assert calculate_triangle_area(5, 6, 7)==15
"""

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (