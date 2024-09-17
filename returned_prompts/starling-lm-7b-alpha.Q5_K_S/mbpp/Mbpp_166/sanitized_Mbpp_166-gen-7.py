def find_even_pair(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] ^ nums[j]) % 2 == 0:
                res += 1
    return res