def reverse_Array_Upto_K(nums: list,k: int) -> list:
    for i in range(k//2):
        nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
    return nums

