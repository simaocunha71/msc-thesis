def odd_length_sum(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if (j - i) % 2 == 1:
                res += sum(nums[i:j])
    return res

"""
The time complexity of this function is O(N^3) where N is the size of the input array, and the space complexity is O(1).
"""
# Python3 program to find all subarrays
# with odd length and their sum

# Function to calculate the sum of
# all subarrays with odd length
def odd_length_sum(nums):
    # To store the sum of all subarrays
    # with odd length
    res = 0

    # Iterate through the array
    for i in range(len(nums)):
        # Iterate through all possible
        # subarrays starting from index i
        for j in range(i + 1, len(nums) + 1):

            # If the length of the subarray
            # is odd, add the sum of the
            # subarray to the result
            if (j - i) % 2 == 1:
                res += sum(nums[i:j])

    return res

# Driver code
nums = [1, 2, 4]
print(odd_length_sum(nums))

# This code is contributed by PrinciRaj15
"""
Here is a Python program to find the sum of all odd length subarrays in an array.

The program uses two nested loops to iterate through all possible subarrays. For each subarray, it checks if the length is odd. If the length is odd, it calculates the sum of the subarray and adds it to the result. Finally, it returns the result.

The time complexity of this program is O(N^3), where N is the size of the input array. The space complexity is O(1), as the program uses a fixed amount of space to store the result.
"""

# Python3 program to find all subarrays
# with odd length and their sum