"""
def count_Primes_nums(nums):
    if nums <= 2:
        return 0
    count = 0
    for i in range(2, nums):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            count += 1
    return count
"""
