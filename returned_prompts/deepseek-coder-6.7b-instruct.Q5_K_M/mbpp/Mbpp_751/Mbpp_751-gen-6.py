"""
Here is a simple way to check if a given array represents a min heap or not. 

In a min heap, each parent node is smaller than its child nodes. So we just need to check if this property holds true for all nodes. 

We can do this by iterating over the array and checking that each parent is smaller than its children. If we find a parent that is larger than its children, we can return False immediately. If we don't find any such parent, then the array represents a min heap.
"""

def check_min_heap(arr):
    n = len(arr)
    for i in range(int(n/2)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and arr[i] > arr[left_child]:
            return False
        if right_child < n and arr[i] > arr[right_child]:
            return False
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6]))  # True
"""
The function starts at the first parent node (at index 0), and for each parent node, it checks if the parent is smaller than its children. If it finds a parent that is larger than its children, it immediately returns False. If it doesn't find any such parent, it returns True, indicating that the array represents a min heap.
"""

