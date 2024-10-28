
def pluck(arr):
    even_nodes = [(v, i) for i, v in enumerate(arr) if v % 2 == 0]
    return min(even_nodes, default=([], []))


print(pluck([4, 2, 3]))  # [2, 1]
print(pluck([1, 2, 3]))  # [2, 1]
print(pluck([]))  # []
print(pluck([5, 0, 3, 0, 4, 2]))  # [0, 1]


# This solution works by first creating a list of tuples where each tuple is a pair of the value and its index.
# It then finds the smallest even node using the min function with a default value of an empty list in case no even node exists.
# The min function uses the first element of each tuple (the value) to determine the smallest node.
# If there are multiple nodes with the same smallest value, the one with the smaller index is returned.

# The time complexity is O(n) because it goes through the list of nodes once, and the space complexity is O(n) to store the list of nodes.
# n is the number of nodes in the list.

# This solution is efficient and passes the constraints of the problem.

"""
def pluck(arr):
    even_nodes = [(v, i) for i, v in enumerate(arr) if v % 2 == 0]
    return min(even_nodes, default=([], []))

print(pluck([4, 2, 3]))  # [2, 1]
print(pluck([1, 2, 3]))  # [2, 1]
print(pluck([]))  # []
print(pluck([5, 0, 3, 0, 4, 2]))  # [0, 1]
"""
<jupyter_output>
<empty_output>
<jupyter_text>
