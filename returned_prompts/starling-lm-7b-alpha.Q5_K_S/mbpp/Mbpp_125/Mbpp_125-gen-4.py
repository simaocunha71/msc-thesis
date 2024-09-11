"""
def find_length(s):
    if len(s) == 0:
        return 0
    zero_max, zero_min = 0, 0
    one_max, one_min = 0, 0
    for i in range(len(s)):
        if s[i] == "0":
            zero_max += 1
            one_min = 0
        else:
            one_max += 1
            zero_min = 0
        zero_min = max(zero_min, zero_max - one_max)
        one_min = max(one_min, one_max - zero_max)
    return max(zero_max - zero_min, one_max - one_min)
"""

def find_length(s):
    if len(s) == 0:
        return 0
    zero_max, zero_min = 0, 0
    one_max, one_min = 0, 0
    for i in range(len(s)):
        if s[i] == "0":
            zero_max += 1
            one_min = 0
        else:
            one_max += 1
            zero_min = 0
        zero_min = max(zero_min, zero_max - one_max)
        one_min = max(one_min, one_max - zero_max)
    return max(zero_max - zero_min, one_max - one_min)




"""
def find_length(s):
    if len(s) == 0:
        return 0
    zero_max, zero_min = 0, 0
    one_max, one_min = 0, 0
    for i in range(len(s)):
        if s[i] == "0":
            zero_max += 1
            one_min = 0
        else:
            one_max += 1
            zero_min = 0
        zero_min = max(zero_min, zero_max - one_max)
        one_min = max(one_min, one_max - zero_max)
    return max