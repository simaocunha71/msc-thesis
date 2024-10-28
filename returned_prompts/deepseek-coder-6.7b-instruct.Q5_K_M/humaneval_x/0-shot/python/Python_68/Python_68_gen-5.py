
def pluck(arr):
    if not arr: return []
    smallest_even = float('inf')
    smallest_even_index = float('inf')
    for index, value in enumerate(arr):
        if value % 2 == 0 and value <= smallest_even:
            smallest_even = value
            smallest_even_index = index
    return [smallest_even, smallest_even_index] if smallest_even != float('inf') else []

# Test cases:
print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]
print(pluck([1, 3, 5, 7, 9])) # []
print(pluck([0, 2, 4, 6, 8])) # [0, 0]
print(pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [2, 1]

# Time complexity: O(n), n is the length of the array
# Space complexity: O(1), no extra space is used.

# This function iterates over the given array once, checking each node for even value and its index,
# then comparing it to the current smallest even value and its index. If a smaller even value is found,
# it is stored, and if the same value is found but with smaller index, it is also stored.
# If no even value is found, an empty list is returned.
<jupyter_output>
[2, 1]
[2, 1]
[]
[0, 1]
[]
[2, 0]
[2, 0]
<jupyter_text>
