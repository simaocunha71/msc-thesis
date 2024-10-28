def find_length(s: str) -> int:
    max_diff = 0
    count_zero = count_one = 0
    for char in s:
        if char == '0':
            count_zero += 1
        else:
            count_one += 1
        diff = count_zero - count_one
        if diff > max_diff:
            max_diff = diff
    return max_diff