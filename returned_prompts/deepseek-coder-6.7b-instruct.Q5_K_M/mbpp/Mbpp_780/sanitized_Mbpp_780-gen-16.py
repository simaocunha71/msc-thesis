def find_combinations(nums):
    results = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            results.append((nums[i][0]+nums[j][0], nums[i][1]+nums[j][1]))
    return results