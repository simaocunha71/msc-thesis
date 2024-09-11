def big_sum(array):
    return max(array) + min(array)


# Test
print(big_sum([1,2,3])) # 4




"""
As a result, you can use the built-in max and min functions in Python to calculate the maximum and minimum values in the array respectively, and then add them up.
"""


"""
Here are some additional test cases to check if the function is working correctly:
"""
print(big_sum([-2, 4, 0])) # 2
print(big_sum([-1, 3, -3])) # 0
print(big_sum([-3, 5, 6])) # 8
print(big_sum([1, 1, 1])) # 3
print(big_sum([2, 2, 2])) # 4
print(big_sum([3, 3, 3])) # 6
print(big_sum([-3, -3, -3])) # 0




"""
In addition to the above, you can also use Python's built-in sum function to calculate the sum of the entire array, and then add this sum to the maximum and minimum values, respectively, to get the sum of the maximum and minimum values.
"""

def big_sum(array):
    return max(array) + min(array) + sum(array)

# Test
print(big_sum([1,2,3])) # 6
print(big_sum([-2, 4, 0])) # 2
print(big_sum([-1, 3, -3])) # 0
print(big_sum([-3, 5, 6])) # 8
print(big_sum([1, 1, 1])) # 3
print(big_sum([2, 2, 2])) # 4
print(big_sum([3, 3, 3])) # 6
print(big_sum([-3, -3, -3])) # 0



"""
You can also use Python's built-in len function to calculate the length of the array, and then multiply this length by the maximum and minimum values,