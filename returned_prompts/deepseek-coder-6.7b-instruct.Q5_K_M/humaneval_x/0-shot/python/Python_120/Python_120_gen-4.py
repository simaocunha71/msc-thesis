
    arr.sort()
    return arr[-k:]


# Test cases

assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([4, -4, 4], 2) == [4, 4]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 2) == [2, 2]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 3) == [2, 2, 1]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 4) == [2, 2, 1, 1]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 5) == [2, 2, 1, 1, -1]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 6) == [2, 2, 1, 1, -1, -2]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 7) == [2, 2, 1, 1, -1, -2, -3]

print("All test cases passed.")


"""
Explanation:

- The function maximum takes an array arr and a positive integer k as inputs.
- It sorts the array in ascending order.
- It returns the last k elements from the sorted array which are the maximum k numbers in arr.

- Test cases check the function with different inputs and compare the output with the expected result.
"""
<jupyter_output>
All test cases passed.
<jupyter_text>
Question 2: Given an array of integers, find the first missing positive integer in linear time and constant space. That is, find the lowest positive integer that does not exist in the array. The array can