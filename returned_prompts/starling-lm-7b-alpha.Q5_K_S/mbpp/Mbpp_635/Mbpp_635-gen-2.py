"""
def heap_sort(nums):
    def heapify(nums, i, heap_size):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, largest, heap_size)

    def build_max_heap(nums):
        heap_size = len(nums)
        for i in range(heap_size // 2, -1, -1):
            heapify(nums, i, heap_size)

    def extract_max():
        nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
        heap_size -= 1
        heapify(nums, 0, heap_size)
        return nums[heap_size]

    build_max_heap(nums)
    while len(nums) > 1:
        extract_max()
    return nums


heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

"""

def heap_sort(nums):
    def heapify(nums, i, heap_size):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < heap_size and nums[left] > nums[largest]:
            largest = left
        if right < heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, largest, heap_size)

    def build_