def larg_nnum(nums: list,n: int) -> list:
    nums.sort(reverse=True)
    return nums[:n]