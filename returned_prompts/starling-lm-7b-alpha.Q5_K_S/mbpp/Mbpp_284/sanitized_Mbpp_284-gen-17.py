def check_element(nums:list,element:list)->bool:
    for i in range(len(nums)):
        if nums[i]!=element:
            return False
    return True