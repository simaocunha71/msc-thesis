
from collections import Counter
def max_occurrences(nums):
    c = Counter(nums)
    return c.most_common(1)[0][0]


