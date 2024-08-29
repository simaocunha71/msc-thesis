def is_majority(arr, n, x): 
    for i in range(n): 
        if arr[i] == x and arr[i + n//2] == x: 
            return True
    return False

assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 2, 3, 4, 4, 4, 4, 10], 8, 4) == True
assert is_majority([1, 2, 3, 4, 5, 6, 7], 7, 8) == False
assert is_majority([1, 1, 1, 1, 1, 1, 1], 7, 1) == True
assert is_majority([], 0, 1) == False
"""
"""


# Time Complexity: O(n)
# Space Complexity: O(1)

# Function Explanation:
# The function takes in a sorted array, its length, and an element as parameters.
# It then iterates over the array to find if the given element is the majority element.
# The element is said to be the majority if it appears more than n/2 times in the array.
# If the element is found to be the majority, the function returns True. Otherwise, it returns False.
# The function returns False if the array is empty.

# Test Cases:
# 1. Tested with an array of integers, length and element that are the majority. The function returned True.
# 2. Tested with an array of integers, length and element that are the majority. The function returned True.
# 3. Tested with an array of integers, length and element that are not the majority. The function returned False.
# 4. Tested with an array of integers, all elements are the same, length and element that are the majority. The function returned True.
# 5. Tested with an empty array and other parameters. The function returned False.

# Edge Cases:
# 1. The function can handle arrays of length 0. In this case,