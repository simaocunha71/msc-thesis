def check_element(lst, elem):
    return all(x == elem for x in lst)

print(check_element(["green", "orange", "black", "white"],'blue'))

"""
This function uses the all() function, which returns True if all items in an iterable are true. In this case, we're using it to check if all items in the list are equal to the given element. If they are, all() returns True; otherwise, it returns False.
"""

