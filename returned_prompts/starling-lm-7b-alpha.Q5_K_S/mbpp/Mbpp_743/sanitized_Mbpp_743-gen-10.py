def rotate_right(nums, k):
    def rotate(nums, k):
        nums.insert(0, nums.pop(len(nums)-k))
    for _ in range(k):
        rotate(nums, 1)
    return nums