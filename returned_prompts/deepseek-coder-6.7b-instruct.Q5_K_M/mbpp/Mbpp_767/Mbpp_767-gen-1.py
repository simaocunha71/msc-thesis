
from collections import defaultdict
def get_pairs_count(arr, sum):
    n = len(arr)
    m = defaultdict(int)
    twice_count = 0

    for i in range(n):
        if arr[i] * 2 == sum:
            twice_count += 1
        m[arr[i]] += 1

    for i in range(n):
        twice_count -= m[sum - arr[i]]

    return twice_count//2


