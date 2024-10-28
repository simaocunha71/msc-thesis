
def max_product(nums):
    asc = []
    for i in range(len(nums)):
        if not asc or nums[i] > asc[-1]:
            asc.append(nums[i])
        elif nums[i] < asc[-1]:
            j = len(asc) - 1
            while j >= 0 and asc[j] < nums[i]:
                j -= 1
            asc[j + 1] = nums[i]
    return asc[-1] * asc[-2]


