def is_num_decagonal(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    decagonal_nums = [27, 100]
    while len(decagonal_nums) < n:
        decagonal_nums.append(sum(decagonal_nums[-1: -2]) + decagonal_nums[-1] + decagonal_nums[-2] + 1)
    return decagonal_nums[n - 1]