def cummulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total

# Test
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Explanation:
# The function cummulative_sum() takes a tuple list as input. It initializes a variable total to zero. Then it iterates over each tuple in the tuple list, and adds up all the values in each tuple to the total. Finally, it returns the total, which is the cumulative sum of all the values in the given tuple list.

"""
Explanation:
In the provided Python code, a function cummulative_sum() is defined, which takes a tuple list as its parameter. The function initializes a variable called total to zero. It then uses a for loop to iterate over each tuple in the tuple list. Inside the loop, the sum() function is used to add up all the values in each tuple and the result is added to the total variable. After all the tuples in the tuple list have been processed, the total variable contains the cumulative sum of all the values in the tuple list. The function then returns this total value.

In the given test case, the function cummulative_sum() is called with the tuple list [(1, 3), (5, 6, 7), (2, 6)]. The function calculates the cumulative sum of all the values in the tuple list, which is 30. The assert statement checks if the result of the function call is equal to the expected value of 30, and if it is, the assertion passes and the test case is considered successful.
"""

# This code is a part of Series "Learn Python from Scratch #11" by tutorials365

# Series Link: https://www.tutorialspoint.com/python/python_functions.htm
# Video Link: https://www.youtube.com/playlist?list=PLzByhoLwt_Yx_GsZJX-_CZ46JjfTt10VD

"""
In the provided Python code, a function