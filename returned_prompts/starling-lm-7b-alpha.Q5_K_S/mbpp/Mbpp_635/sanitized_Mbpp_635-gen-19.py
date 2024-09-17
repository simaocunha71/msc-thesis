def heap_sort(nums: list) -> list:
    hq.heapify(nums)
    for i in range(len(nums)-1, 0, -1):
        hq.heapreplace(nums, nums[i])
    return nums