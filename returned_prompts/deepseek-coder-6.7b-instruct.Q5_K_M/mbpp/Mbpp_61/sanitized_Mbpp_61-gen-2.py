def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum_digits = 0
        for j in range(i, len(s)):
            sum_digits += int(s[j])
            if sum_digits == j - i + 1:
                count += 1
    return count