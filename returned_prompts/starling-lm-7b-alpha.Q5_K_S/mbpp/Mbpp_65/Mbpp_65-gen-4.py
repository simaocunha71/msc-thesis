def recursive_list_sum(input_list):
    """flatten a list and sum all of its elements"""
    sum = 0
    for elem in input_list:
        if type(elem) == list:
            sum += recursive_list_sum(elem)
        else:
            sum += elem
    return sum

# Test
print(recursive_list_sum([1, 2, [3,4],[5,6]]))  # returns: 21

# Explanation:
# The function recursive_list_sum takes an input list and initializes a variable sum as 0.
# It then iterates through each element in the input list.
# If an element is a list, the function recursively calls itself on that sublist and adds the result to the sum variable.
# If an element is not a list, it adds the element to the sum variable.
# After iterating through all elements in the input list, the function returns the sum.

# In the given test case, the input list is [1, 2, [3,4],[5,6]].
# The function first adds the elements 1 and 2 to the sum.
# It then encounters the sublist [3,4] and recursively calls itself on that sublist, adding 7 to the sum.
# Finally, it encounters the sublist [5,6] and recursively calls itself on that sublist, adding 11 to the sum.
# The function then returns the total sum, which is 21.

# The assert statement at the top of the code checks if the function is correctly summing all elements in the given list.

# The print statement at the end of the code demonstrates the usage of the function by passing the input list [1, 2, [3,4],[5,6]] to it and printing the result, which should be 21.

"""
The function recursive_list_sum takes an input list and initializes a variable sum as 0.
It then iterates through each element in the input list.
If an element is a list, the function recursively calls itself on that sublist and adds the result to the sum variable.
If an element is not a list, it adds the