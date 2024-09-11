"""
def heap_sort(nums):
    def max_heapify(nums, root, heap_size):
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != root:
            nums[largest], nums[root] = nums[root], nums[largest]
            max_heapify(nums, largest, heap_size)

    def build_max_heap(nums):
        heap_size = len(nums)
        for i in range(len(nums) // 2, -1, -1):
            max_heapify(nums, i, heap_size)

    def heap_sort(nums):
        build_max_heap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(nums, 0, i)
    return nums
"""

def heap_sort(nums):
    def max_heapify(nums, root, heap_size):
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != root:
            nums[largest], nums[root] = nums[root], nums[largest]
            max_heapify(nums, largest, heap_size)

    def build_max_heap(nums):
        heap_size = len(nums)
        for i in range(len(nums) // 2, -1, -1):
            max_heapify(