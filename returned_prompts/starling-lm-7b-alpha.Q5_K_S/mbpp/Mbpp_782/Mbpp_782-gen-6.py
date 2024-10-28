
def odd_length_sum(nums: list):
    result = 0
    for i in range(len(nums)):
        result += sum(nums[j] for j in range(i,len(nums))) + 1
    return result


