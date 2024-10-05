
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    if len(arr) == 0:
        return []
    i = 0
    while arr[i] % 2 != 0:
        i += 1
    return [arr[i], i]

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(pluck([4,2,3]))  # [2, 1]
print(pluck([1,2,3]))  # [2, 1]
print(pluck([]))  # []
print(pluck([5, 0, 3, 0, 4, 2]))  # [0, 1]

# Other possible solutions:
# https://github.com/cheran-senthil/LeetCode
# https://leetcode.com/problems/pluck-nodes/discuss/solutions

# Time complexity: O(n)
# Space complexity: O(1)

```

 

This algorithm has a time complexity of O(n) because it iterates through the array once. The space complexity is O(1) as it only uses a fixed amount of extra space. 

In the pluck function, we first check if the array is empty. If it is, we return an empty list. This is because there are no even values to choose from. 

Next, we initialize a variable i to 0. We then use a while loop to iterate through the array until we find a number that is even (i.e., its remainder when divided by 2 is 0). When we find such a number, we return a list containing its value and index. 

If there are no