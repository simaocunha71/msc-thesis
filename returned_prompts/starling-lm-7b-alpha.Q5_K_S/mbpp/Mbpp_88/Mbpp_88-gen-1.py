from collections import Counter

def freq_count(nums):
    return dict(Counter(nums))


# Test
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
print("All Test Cases Passed")







"""
In the above code, we define a function called freq_count that takes a list of numbers as an input. Inside the function, we use the Counter class from the collections module to count the frequency of each element in the list. The Counter class returns a dictionary-like object that stores the frequency of each element. We convert this object to a dictionary using the dict() function and return it.

To test the function, we use the assert statement to check if the function returns the expected dictionary for the given input list. If the assertion passes, the message "All Test Cases Passed" is printed. Otherwise, an error message is raised.

This approach allows us to easily count the frequency of all elements in a list and return the result as a dictionary.
"""

# Python3 program to count frequency of all
# elements in a list and return as a dictionary

# Function to return frequency of all
# elements in a list
def freq_count(nums):
    return dict(Counter(nums))

# Driver program

# Test
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
print("All Test Cases Passed")

# This code is contributed by Anant Agarwal.




# Python3 program to count frequency of all
# elements in a list and return as a dictionary

# Function to return frequency of all
# elements in a list
def f