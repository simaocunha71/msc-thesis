def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest([10, 20, 40, 50, 30]))

# Output: 40

# Explanation: The function sorts the list in ascending order and then returns the second last element which is the second largest number.

"""
Write a Python function that checks whether a given string is a pangram or not. 
A pangram is