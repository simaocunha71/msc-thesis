def count_Substrings(s):
    def is_valid(i, j):
        digit_sum = sum(int(c) for c in s[i:j+1])
        return digit_sum == j - i + 1

    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_valid(i, j):
                count += 1
    return count