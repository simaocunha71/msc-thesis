def remove_elements(nums, to_remove):
    return [i for i in nums if i not in to_remove]  # or nums[:] = [i for i in nums if i not in to_remove] for in-place modification