from collections import defaultdict
def largest_subset(nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num % 2] += 1
    return max(counts.values())