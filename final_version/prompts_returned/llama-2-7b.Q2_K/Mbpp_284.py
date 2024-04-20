"""
Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.
assert check_element(["green", "orange", "black", "white"],'blue')==False
"""

def check_element(list, element):
    for i, item in enumerate(' '.join(list)):
        if item != element:
            return False  # Returns false if any list elements are not equal to the given element.
    else:
        return True  # Else returns true indicating all items in the given list are equal to element.
