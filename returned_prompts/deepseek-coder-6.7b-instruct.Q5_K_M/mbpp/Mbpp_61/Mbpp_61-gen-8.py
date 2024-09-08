def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum_val = 0
        for j in range(i, len(s)):
            sum_val += int(s[j])
            if sum_val == j - i + 1:
                count += 1
    return count

print(count_Substrings('112112'))  # 6




