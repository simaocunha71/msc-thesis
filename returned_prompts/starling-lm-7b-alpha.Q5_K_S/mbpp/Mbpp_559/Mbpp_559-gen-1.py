
def max_sub_array_sum(nums: list,n: int) -> int:
    max_so_far = 0
    max_ending_here = 0
    for num in nums:
        max_ending_here = max_ending_here + num
        if max_ending_here < 0:
            max_ending_here = 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far


