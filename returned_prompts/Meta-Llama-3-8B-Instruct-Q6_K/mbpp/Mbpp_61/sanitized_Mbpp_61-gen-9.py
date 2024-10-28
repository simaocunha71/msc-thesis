def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        current_sum = 0
        for j in range(i, len(s)):
            current_sum += int(s[j])
            if current_sum == j - i + 1:
                count += 1
    return count