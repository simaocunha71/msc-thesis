
def sort_array(arr):
    def count_ones(n):
        return bin(n).count('1')
    return sorted(arr, key=lambda n: (count_ones(n), n))

# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

In this solution, we defined a helper function count_ones that counts the number of ones in the binary representation of a given number.
Then we used sorted() with a key that is a tuple. In the key, we specified count_ones(n) to sort by the number of ones in the binary representation
and n to sort by the decimal value of the number. This way, if the number of ones is the same, the decimal value will be used to sort.
"""

# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

# Solution:
# The solution works by first converting each number in the list to its binary representation and counting the number of '1's in the binary representation.
# This is done using the built-in count() function.
# The numbers are then sorted in ascending order based on the number of '1's and the decimal value of the numbers.
# This is done using the sorted() function with a custom key function that returns a tuple containing the number of '1's and the decimal value of the number.
# The sorted() function sorts