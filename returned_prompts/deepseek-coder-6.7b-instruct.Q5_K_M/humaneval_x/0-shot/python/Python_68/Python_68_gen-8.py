
def pluck(arr):
    smallest_even = [float('inf'), -1]
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even[0]:
            smallest_even = [num, i]
    return smallest_even if smallest_even[1] >= 0 else []

# Test cases
print(pluck([4,2,3]))  # should return [2, 1]
print(pluck([1,2,3]))  # should return [2, 1]
print(pluck([]))  # should return []
print(pluck([5, 0, 3, 0, 4, 2]))  # should return [0, 1]

# Time Complexity: O(n) - where n is the number of nodes in the tree. This is because we're looping through the array to find the smallest even value.
# Space Complexity: O(1) - we are using constant space to store the smallest even value and its index. This is because we're not using any additional data structures that scale with the size of the input.

# This solution is efficient as it only requires a single pass through the array to find the smallest even value.
# It also handles edge cases such as an empty array correctly.
<jupyter_output>
[2, 1]
[2, 1]
[]
[0, 1]
<jupyter_text>
Problem 2: Minimum Time to Make Rope Colorful (Medium)Given an array of integers `arr` and an integer `k`, and two integers `a` and `b`. You can flip the colors of the array for a cost of `k` at most. Return the minimum possible cost to make all the elements of the array equal to either `a` or `b`.The cost of flipping a color is `k` if the colors of the two adjacent elements are different (or there is no adjacent element), and `0` otherwise.
<jupyter_code>
