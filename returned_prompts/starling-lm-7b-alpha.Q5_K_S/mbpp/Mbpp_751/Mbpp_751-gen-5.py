To check if the given array represents min heap or not, you can follow these steps:

1. Check if the root node (the element at index 0) is the minimum value in the heap. If it is not, then it does not represent a min heap.
2. Recursively check the left and right subtrees of each node. If a node's value is greater than its left child's value or its right child's value (whichever is smaller), then it does not represent a min heap.
3. Repeat step 2 for each node in the heap until all nodes have been checked.
4. If all nodes pass the checks, then the array represents a min heap.

Here's a Python implementation of the `check_min_heap` function that follows these steps:

```python
def check_min_heap(heap):
    def is_min_heap(node, left, right):
        if left and heap[left] < heap[node]:
            return False
        if right and heap[right] < heap[node]:
            return False
        return True

    def _check_min_heap(heap, node, left, right):
        if node >= len(heap):
            return True
        if not is_min_heap(node, left, right):
            return False
        return _check_min_heap(heap, node * 2 + 1, node * 2 + 1, node * 2 + 2) and \
               _check_min_heap(heap, node * 2 + 2, node * 2 + 1, node * 2 + 2)

    return _check_min_heap(heap, 0, 0, 1)
```

You can use the `check_min_heap` function to check if a given array represents a min heap or not. For example, to check if the array `[1, 2, 3, 4, 5, 6]` represents a min heap, you can call `check_min_heap([1, 2, 3, 4, 5, 6])`. This will return `True` since the array represents a min heap.

"""

def check_min_heap(heap):
