from collections import deque
import unittest
def max_sum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    inc = [1] * n
    dec = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                inc[i] = max(inc[i], inc[j] + 1)
            if nums[i] < nums[j]:
                dec[i] = max(dec[i], dec[j] + 1)
    max_val = 0
    q = deque()
    for i in range(n - 1, -1, -1):
        while q and q[-1] < dec[i]:
            q.pop()
        q.append(dec[i])
        max_val = max(max_val, sum(q))
    return max_val