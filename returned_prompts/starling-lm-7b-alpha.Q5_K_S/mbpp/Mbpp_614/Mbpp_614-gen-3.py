def cummulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total

def test_cummulative_sum():
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30

test_cummulative_sum()






"""
In this function, we have a list of tuples. We initialize a total variable to 0. Then, using a for loop, we iterate over each tuple in the list. In each iteration, we add the sum of the values of the current tuple to the total. Finally, we return the total, which is the cumulative sum of all the values in the list of tuples.
"""

"""
The function assert is used to check if a condition is true. In this case, we are checking if the cummulative_sum function returns the expected result for the given test case, which is [(1, 3), (5, 6, 7), (2, 6)]. If the condition is true, the assert statement does nothing. If the condition is false, an AssertionError is raised, indicating that the test case failed.
"""

"""
To test the cummulative_sum function, we have a separate function called test_cummulative_sum. Inside this function, we call the cummulative_sum function with the given test case and check if the result is equal to the expected result (30 in this case). If the result is correct, the assert statement does nothing. If the result is incorrect, an AssertionError is raised, indicating that the test case failed.
"""

"""
By running the test_cummulative_sum function, we can verify that the cummulative_sum function works correctly for the given test case. If the test case fails, an error message will be printed, indicating the actual and expected results. If the test case passes, no error message will be printed.
"""

"""
In this case, since the test case passes, no error message will be printed. This means that the cummulative_sum function correctly calculates the cumulative sum of all the values in the given tuple list.
"""




