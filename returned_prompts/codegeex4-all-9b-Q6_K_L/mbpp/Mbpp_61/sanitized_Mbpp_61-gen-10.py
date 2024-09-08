def count_Substrings(s):
    def check(s):
        digit_sum = sum(int(c) for c in s)
        return digit_sum == len(s)

    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if check(s[i:j]):
                count += 1
    return count