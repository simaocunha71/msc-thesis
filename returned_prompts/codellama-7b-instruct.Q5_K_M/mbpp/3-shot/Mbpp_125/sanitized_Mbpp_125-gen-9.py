def find_length(binary_str: str) -> int:
    count_0 = 0
    count_1 = 0
    max_diff = 0
    for char in binary_str:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
        else:
            continue
        max_diff = max(max_diff, abs(count_0 - count_1))
    return max_diff