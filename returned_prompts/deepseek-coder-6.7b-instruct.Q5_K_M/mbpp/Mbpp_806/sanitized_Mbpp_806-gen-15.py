def max_run_uppercase(s):
    max_len = cur_len = 0
    for char in s:
        if char.isupper():
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 0
    return max_len