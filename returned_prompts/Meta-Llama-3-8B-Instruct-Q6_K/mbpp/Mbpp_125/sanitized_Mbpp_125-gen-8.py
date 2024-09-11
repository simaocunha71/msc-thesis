def find_length(s):
    max_diff = 0
    diff = 0
    for char in s:
        if char == '0':
            diff -= 1
        else:
            diff += 1
        max_diff = max(max_diff, abs(diff))
    return max_diff