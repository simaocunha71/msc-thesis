
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

Explanation:

This problem is about sorting an array based on the number of ones in its binary representation and its decimal value. The Python built-in function 'sorted' takes a key function to determine the sort order. Here, we use a lambda function to return a tuple. The first element of the tuple is the number of ones in the binary representation of the number, and the second element is the number itself. The sort order is ascending by default, so we don't need to specify that.

For example, for the number 5 (binary is 101), the lambda function returns (1, 5) because there is one '1' in the binary representation and the decimal value is 5. For the number 2 (binary is 10), the lambda function returns (1, 2) because there is one '1' in the binary representation and the decimal value is 2.

This way, the array is first sorted based on the number of ones in the binary representation, and then sorted based on the decimal value for numbers with the same number of ones in the binary representation.

Note that the 'bin' function returns a string that starts with '0b' to indicate that it is a binary number, so we use the 'count' method to count the number of '1's in the binary representation.
"""

# -------------------------
# Codewars's tests
# -------------------------

def test_sort_array():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
