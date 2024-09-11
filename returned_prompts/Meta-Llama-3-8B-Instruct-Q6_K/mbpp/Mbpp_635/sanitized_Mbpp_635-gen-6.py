from heapq import _heapify, heappop, heappush
def heap_sort(nums):
    heap = nums[:]
    _heapify(heap)
    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
    return sorted_nums[::-1]  # reverse the list to get the original order