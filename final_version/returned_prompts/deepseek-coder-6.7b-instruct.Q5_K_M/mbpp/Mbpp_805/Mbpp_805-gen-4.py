def max_sum_list(lst):
    return max(lst, key=sum)

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

# Output: [10, 11, 12]


# The max function is used to find the maximum value in an iterable or two or more arguments. When used with the key parameter, max function computes the maximum of the iterable based on the key function.

# In this case, we use the sum function as the key function, which returns the sum of the elements in each sublist. The list with the maximum sum is returned by the function.


# Note: The max function returns the first maximum value it finds, so if there are multiple lists with the same maximum sum, it will return the first one.
<jupyter_output>
[10, 11, 12]
<jupyter_text>
Problem 2:
<jupyter_code>
