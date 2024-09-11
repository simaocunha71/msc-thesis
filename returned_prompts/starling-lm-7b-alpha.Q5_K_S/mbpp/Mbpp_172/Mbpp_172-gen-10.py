def count_occurance(s):
    """
    Parameters:
    s (str): The string to be examined

    Returns:
    int: The number of times 'std' appears in the string
    """
    return s.count('std')

# Test
assert count_occurance("letstdlenstdporstd") == 3
print("Passed all tests.")






















"""
In this problem, we are asked to write a function that counts the number of times the string 'std' appears in a given string. The function takes a single parameter, s, which is the string to be examined. The function returns an integer representing the number of times 'std' appears in the string. 

To solve this problem, we can use the built-in count() method in Python, which returns the number of occurrences of a substring in a string. In this case, we can simply call s.count('std') to get the count of occurrences of 'std' in the string s. 

The provided test case, count_occurance("letstdlenstdporstd"), is used to verify the correctness of the function. The expected output is 3, indicating that the string 'std' appears 3 times in the given string. 

Finally, the function is tested and it passes all the tests, indicating that the function is correct and can be used to count the occurrence of a substring in a string.
"""

# Here is a Python program that solves the problem:

"""
def count_occurance(s):
    """
    Parameters:
    s (str): The string to be examined

    Returns:
    int: The number of times 'std' appears in the string
    """
    return s.count('std')

# Test
assert count_occurance("letstdlenstdporstd") == 3
print("Passed all tests.")
"""

# This program defines a function called count_occurance that takes a string s as a parameter. Inside the function, the built-in count() method is used to count the number of occurrences of the substring 'std' in the string s. The result is returned as