
def pair_xor_Sum(nums: list,n: int) -> int:
    return sum(nums[i]^nums[j] for i in range(n) for j in range(i+1,n))


