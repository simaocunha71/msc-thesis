"""
def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(nums, i, n)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)
    return nums

def max_heapify(nums, i, heap_size):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < heap_size and nums[left] > nums[largest]:
        largest = left
    if right < heap_size and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(nums, largest, heap_size)
"""

def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(nums, i, n)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)
    return nums

def max_heapify(nums, i, heap_size):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < heap_size and nums[left] > nums[largest]:
        largest = left
    if right < heap_size and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(num