def check_min_heap(arr):
    # if array is empty
    if len(arr) == 0:
        return True

    # traverse for all nodes in heap
    for i in range(len(arr)):
        # left child
        left = (i + 1) * 2 - 1
        # right child
        right = (i + 1) * 2
        # left child is present in heap and its value is greater than parent node
        if left < len(arr) and arr[left] < arr[i]:
            return False
        # right child is present in heap and its value is greater than parent node
        if right < len(arr) and arr[right] < arr[i]:
            return False

    return True

"""
To check if a heap is a min heap, we compare each node with its children. If a node's value is less than the minimum of its children, the heap is not a min heap.

In this code, we first check if the array is empty, and if so, return True, as an empty array is considered a valid min heap.

Then, we iterate through all nodes in the heap. For each node, we calculate the indices of its left and right child. If the left child exists and its value is greater than the parent node's value, or if the right child exists and its value is greater than the parent node's value, we return False, as the heap is not a min heap.

If we complete the iteration without finding any violations, we return True, indicating that the array represents a valid min heap.
"""
# Python3 program to check if a given array
# is a min heap or not

# Python3 program to check if a given array
# is a min heap or not

"""
To check if a heap is a min heap, we compare each node with its children. If a node's value is less than the minimum of its children, the heap is not a min heap.

In this code, we first check if the array is empty, and if so, return True, as an empty array is considered a valid min heap.

Then, we iterate through all nodes in the heap. For each node, we calculate the indices of its left and right child. If the left