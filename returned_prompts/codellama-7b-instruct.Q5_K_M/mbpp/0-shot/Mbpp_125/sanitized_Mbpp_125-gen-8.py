def find_length(s):
    count = 0
    result = 0
    for c in s:
        if c == '0':
            count += 1
        else:
            result = max(result, count)
            count = 0
    return max(result, count)