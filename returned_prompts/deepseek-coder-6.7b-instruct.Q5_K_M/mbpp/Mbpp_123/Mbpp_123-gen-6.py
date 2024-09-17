
def amicable_numbers_sum(limit):
    nums = [0] * (limit+1)
    for i in range(1, limit+1):
        for j in range(i*2, limit+1, i):
            nums[j] += i
    return sum(x for x in nums if x <= limit and nums[x] != x and nums[nums[x]] == x)


