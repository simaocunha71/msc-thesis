
def pluck(arr):
    min_even_node = [float('inf'), -1]
    for i, node in enumerate(arr):
        if node % 2 == 0 and node < min_even_node[0]:
            min_even_node = [node, i]
    return min_even_node if min_even_node[1] >= 0 else []

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]

Explanation:
The function `pluck` iterates through the given array `arr` and checks each node if it is an even number and smaller than the current smallest even number. If it is, the current node is updated to be the new smallest even number. The function finally returns the smallest even number and its index as a list in the format [node, index], or an empty list if no even number was found.

The time complexity of this solution is O(n), where n is the length of the array `arr`, as it needs to iterate through the array once to find the smallest even number. The space complexity is O(1), as it only requires a constant amount of space to store the smallest even number and its index.

The function passes all the provided test cases.
"""

# 2.
"""
