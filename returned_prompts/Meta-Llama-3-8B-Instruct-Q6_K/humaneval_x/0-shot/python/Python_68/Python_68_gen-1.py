The problem can be solved by iterating over the array and keeping track of the smallest even value and its index. Here's a Python solution for the problem:

```Python
def pluck(arr):
    smallest_even = []
    for i, node in enumerate(arr):
        if node % 2 == 0 and (not smallest_even or node < smallest_even[0]):
            smallest_even = [node, i]
    return smallest_even if smallest_even else []
```

In this solution, we initialize an empty list `smallest_even` to store the smallest even value and its index. We then iterate over the array using `enumerate` to get both the index and the value of each node. If the node is even and its value is smaller than the current smallest even value, we update `smallest_even` with the new smallest even value and its index. Finally, we return `smallest_even` if it's not empty, otherwise we return an empty list. This solution has a time complexity of O(n) where n is the length of the array, and a space complexity of O(1) as we only use a constant amount of space to store the smallest even value and its index. 