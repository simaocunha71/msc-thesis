def check_element(nums, elem):
    for num in nums:
        if num != elem:
            return False
    return True