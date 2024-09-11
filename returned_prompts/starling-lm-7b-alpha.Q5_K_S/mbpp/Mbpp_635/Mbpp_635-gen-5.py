"""
To heapify a max heap, we need to make sure that every node is greater than its children.
Here is a function to heapify the given list:

def heapify(nums, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < size and nums[left] > nums[largest]:
        largest = left
    if right < size and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, largest, size)
"""

"""
To sort the given list using heap sort, first build a max heap, then repeatedly extract the maximum element and place it at the end of the list. Here is the function to implement this:

def heap_sort(nums):
    size = len(nums)
    for i in range(size // 2 - 1, -1, -1):
        heapify(nums, i, size)
    for i in range(size - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)
    return nums
"""

"""
In the above function, for each node, we only need to compare it with its children. However, this is not the most efficient way to compare.
A more efficient way is to first compare the two children and then compare the larger child with the node. Here is an improved version of the function:

def heapify(nums, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < size and nums[left] > nums[largest]:
        largest = left
    if right < size and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
