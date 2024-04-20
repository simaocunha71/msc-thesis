"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""

def Split(list):
    result = []
    for index in list:
        if index % 2 == 0:
            result += [index]
    return result


print(Split([1,3,2,5]))