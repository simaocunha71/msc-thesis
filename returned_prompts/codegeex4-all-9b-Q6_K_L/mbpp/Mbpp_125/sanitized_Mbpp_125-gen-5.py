def find_length(s: str) -> int:
    """Find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string."""
    max_diff = 0
    count_0s = 0
    count_1s = 0
    for c in s:
        if c == '0':
            count_0s += 1
        else:
            count_1s += 1
        max_diff = max(max_diff, abs(count_0s - count_1s))
    return max_diff