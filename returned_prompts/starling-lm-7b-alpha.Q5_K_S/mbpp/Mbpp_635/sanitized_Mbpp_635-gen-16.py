def heap_sort(nums: list):
    n = len(nums)
    for i in range(n//2 - 1, -1, -1):
        heapify(nums, i, n)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)
    return nums