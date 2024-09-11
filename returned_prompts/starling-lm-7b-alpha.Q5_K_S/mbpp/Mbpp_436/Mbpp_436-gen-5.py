def neg_nos(lst):
    res = [x for x in lst if x < 0]
    return res

# Testing the function
print(neg_nos([-1,4,5,-6])) # should print [-1, -6]




"""
As a programmer, you are given a list of numbers. Your task is to write a function that will return a list of all negative numbers from the original list.

Here are the steps to take in order to solve this problem:

    Define a function named neg_nos that takes a list of numbers as an input parameter.
    Create an empty list named res.
    Iterate through the given list of numbers and check if the current number is less than zero. If it is, add the number to the res list. If it is not, skip the number.
    Return the res list.

The provided code already defines the function and creates an empty list named res. The function uses list comprehension to iterate through the given list and checks if the current number is less than zero. If it is, the number is added to the res list. If it is not, the number is skipped.

To test the function, the code calls the neg_nos function with a sample list of numbers [ -1, 4, 5, -6 ] and prints the result. The expected output is [-1, -6], which are the negative numbers in the original list.
"""

"""
The provided code defines a function named neg_nos that takes a list of numbers as an input parameter. The function uses list comprehension to create a new list that contains only the negative numbers from the original list. The function returns this new list.

To test the function, the code calls the neg_nos function with a sample list of numbers [ -1, 4, 5, -6 ] and prints the result. The expected output is [-1, -6], which are the negative numbers in the original list.
"""

"""
The provided code defines a function named neg_nos that takes a list of numbers as an input parameter. The function uses a for loop to iterate through the given list of numbers and checks if the current number is less than zero. If it is, the number is added to the res list. If it is not, the number is skipped. The