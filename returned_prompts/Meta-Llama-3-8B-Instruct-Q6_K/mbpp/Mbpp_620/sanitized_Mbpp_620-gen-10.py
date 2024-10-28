def largest_subset(nums):
    from collections import defaultdict
    d = defaultdict(int)
    for num in nums:
        for i in range(2, num + 1):
            if num % i == 0:
                d[i] += 1
    max_size = 0
    for key, value in d.items():
        max_size = max(max_size, value + 1)
    return max_size