def heap_sort(nums:list)->list:
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, i)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0)
    return nums