"""
def count(lst):
    c = 0
    for i in lst:
        if i == True:
            c += 1
    return c
"""

def count(lst):
    return sum(map(lambda x: x==True, lst))

# Test Case
assert count([True,False, True]) == 2

# Other Test Cases
print(count([True, False]))
print(count([True, True, True]))
print(count([False, False, False]))
print(count([False, True, False]))

"""
The given function should return the count of true boolean values in the given list.

The function is correct. It uses a for loop to iterate over the list and a if statement to check if each element is True. If the element is True, the function increments the count variable. After iterating over the entire list, the function returns the count.

The function also includes a test case to check if the function correctly counts the true boolean values in a list. The function correctly counts the true boolean values in the given list, as the test case asserts.

The function can handle lists of any length and with any combination of True and False values. This is demonstrated by the additional test cases, which show that the function correctly counts the true boolean values in lists with different combinations of True and False values.
"""

"""
This program defines a function `count` that takes a list as input and returns the count of true boolean values in the list. The function uses a for loop to iterate over the list and a if statement to check if each element is True. If the element is True, the function increments a counter variable. After iterating over the entire list, the function returns the counter variable, which represents the count of true boolean values in the list.

The program includes an assertion to verify the correctness of the function. The assertion checks if the function correctly counts the true boolean values in a given list, and the assertion should pass if the function is working correctly.

The program also includes additional test cases to demonstrate the functionality of the function. These test cases show that the function correctly counts the true boolean values in lists with different combinations of True and False values.
"""

"""
The program defines a function `count` that takes a list of boolean values as