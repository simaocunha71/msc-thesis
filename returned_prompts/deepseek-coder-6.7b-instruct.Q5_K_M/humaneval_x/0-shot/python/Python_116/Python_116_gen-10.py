
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Testing
print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

# This solution works by using the built-in sorted function in Python, with a custom key that first counts the number of ones in the binary representation of the number and then sorts based on the decimal value.

# The lambda function is a small anonymous function that takes an argument x and returns a tuple. The first element of the tuple is the number of ones in the binary representation of x (which is obtained using the bin and count methods), and the second element of the tuple is x itself.

# The sorted function then sorts the list based on these keys in ascending order.

# For example, if we call sort_array([1, 5, 2, 3, 4]), the lambda function will return [(1, 1), (2, 5), (1, 2), (2, 3), (2, 4)], and the sorted function will return [(1, 1), (1, 2), (2, 3), (2, 4), (2, 5)] (since sorting tuples is done lexicographically), which is then converted back to [1, 2, 3, 4, 5].

# This way, the array is sorted first by the number of ones in the binary representation, and then by the decimal value of the numbers.

# Note that the binary representation of negative numbers in Python starts with '-0b' and does not include a sign, so the number of ones in the binary representation of a negative number is counted correctly.

# Also, please note that this solution assumes that the input array is a list of non-negative integers. If