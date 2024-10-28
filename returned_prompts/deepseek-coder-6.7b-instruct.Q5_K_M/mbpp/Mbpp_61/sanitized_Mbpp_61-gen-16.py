def count_Substrings(s):
    counter, sub_sum, sub_len = 0, 0, 0
    for i in range(len(s)):
        sub_sum += int(s[i])
        sub_len += 1
        if sub_sum == sub_len:
            counter += 1
        if sub_sum > sub_len:
            sub_sum, sub_len = int(s[i]), 1
    return counter