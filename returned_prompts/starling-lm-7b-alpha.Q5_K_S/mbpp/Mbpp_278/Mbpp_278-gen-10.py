def count_first_elements(tup):
    return sum(map(lambda x: len(x), tup))


# Alternate solution
def count_first_elements(tup):
    return sum(map(len, tup))

# Testing the function
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
print("All Tests Passed")






"""
In this problem, we have to find the number of elements that occur in the given tuple. We can use the built-in len() function to find the length of each element in the tuple and then sum up all the lengths. This can be done using the map() function along with a lambda function to apply the len() function to each element in the tuple, and then summing up the results using the sum() function. We can wrap this in a function called count_first_elements() to make it reusable.

To test the function, we can use the assert statement to check if the result of the function is equal to the expected result. In this case, the expected result is 3, so we can use assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3 to check if the function is working correctly. If all the tests pass, the message "All Tests Passed" will be printed.

Note: The solution uses the map() function, which applies a given function to each item of an iterable and returns a list of the results. In this case, we are using the map() function to apply the len() function to each element in the tuple.
"""

"""
Here is a step-by-step explanation of the solution:

1. Define a function called count_first_elements that takes a tuple as an argument.
2. Use the map() function to apply the len() function to each element in the tuple. This will return a list of the lengths of the elements.
3. Use the sum() function to sum up all the lengths in the list. This will give us the total number of elements in the tuple.
4. Return the result from the function.
5. Use the assert statement to check if the result of the function is equal to the expected result (3 in this case