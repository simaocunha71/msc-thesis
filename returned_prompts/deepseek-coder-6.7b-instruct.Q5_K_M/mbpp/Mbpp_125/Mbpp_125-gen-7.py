
def find_length(s: str) -> int:
    max_diff = 0
    count_zero = count_one = 0
    for char in s:
        if char == '0':
            count_zero += 1
        else:
            count_one += 1
        max_diff = max(max_diff, abs(count_zero - count_one))
    return max_diff


