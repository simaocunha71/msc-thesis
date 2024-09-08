def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas_nums = [2, 1]
    for i in range(2, n + 1):
        lucas_nums.append(lucas_nums[i - 1] + lucas_nums[i - 2])
    return lucas_nums[n]

print(find_lucas(9))  # should return 76

