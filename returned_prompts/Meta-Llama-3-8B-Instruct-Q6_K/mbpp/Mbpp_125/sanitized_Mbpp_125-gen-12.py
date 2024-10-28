def find_length(s):
    max_diff = 0
    zero_count = 0
    one_count = 0
    for i in range(len(s)):
        if s[i] == '0':
            zero_count += 1
        else:
            one_count += 1
        max_diff = max(max_diff, abs(zero_count - one_count))
    return max_diff