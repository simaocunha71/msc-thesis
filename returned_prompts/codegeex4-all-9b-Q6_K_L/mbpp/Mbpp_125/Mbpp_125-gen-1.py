def find_length(s: str) -> int:
    max_diff = 0
    count_0 = 0
    count_1 = 0
    for c in s:
        if c == '0':
            count_0 += 1
        elif c == '1':
            count_1 += 1
        max_diff = max(max_diff, abs(count_0 - count_1))
    return max_diff

