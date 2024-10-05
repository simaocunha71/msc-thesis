
def pluck(arr):
    smallest_even = [float('inf'), -1]
    smallest_index = [float('inf'), -1]
    
    for i, n in enumerate(arr):
        if n % 2 == 0:
            if n < smallest_even[0]:
                smallest_even = [n, i]
            elif n == smallest_even[0] and i < smallest_even[1]:
                smallest_even = [n, i]
                
        if n < smallest_index[0]:
            smallest_index = [n, i]
        elif n == smallest_index[0] and i < smallest_index[1]:
            smallest_index = [n, i]

    return smallest_even if smallest_even[0] != float('inf') else (smallest_index if smallest_index[0] != float('inf') else [])

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]

# Complexity:
# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# This solution iterates over the array twice. In the first pass, it looks for the smallest even value and its index.
# In the second pass, it looks for the smallest value and its index.
# If there is no even number, it will return the smallest value found in the first pass. If there are no values, it will return an empty list.

# If there are multiple smallest values, it will return the one with the smallest index.
# This is done by checking if the current value is smaller than the smallest found so far, or if it is the same but has a smaller index.
# If no smallest values are found at all, an empty list is returned.

# This solution is efficient because it only needs to iterate over the array once, and it uses constant extra space.
# The time complexity is linear due to the single iteration over the array, and the space