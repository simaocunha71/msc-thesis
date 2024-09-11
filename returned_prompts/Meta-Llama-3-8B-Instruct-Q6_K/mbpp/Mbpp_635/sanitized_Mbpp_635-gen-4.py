import heapq
def heap_sort(nums: list) -> list:
    return list(heapq.heapify(nums))
    # heapq.heapify(nums)
    # return nums