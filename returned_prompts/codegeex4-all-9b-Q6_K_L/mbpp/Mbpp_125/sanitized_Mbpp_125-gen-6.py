def find_length(s):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    start = 0

    for i in range(len(s)):
        if s[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

        if count_0 > count_1:
            count_0 -= 1
            count_1 -= 1
            start += 1
        elif count_0 < count_1:
            count_0 += 1
            count_1 -= 1

        max_diff = max(max_diff, count_0 - count_1)

    return max_diff