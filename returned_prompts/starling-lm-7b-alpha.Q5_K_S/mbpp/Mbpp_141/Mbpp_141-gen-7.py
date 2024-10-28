
def pancake_sort(nums:list) -> list:
    for i in range(len(nums) - 1, 0, -1):
        max_element = max(nums[:i + 1])
        index = nums[:i + 1].index(max_element)
        nums[:index + 1], nums[index + 1: i + 1] = nums[index + 1: i + 1], nums[:index + 1]
    return nums


