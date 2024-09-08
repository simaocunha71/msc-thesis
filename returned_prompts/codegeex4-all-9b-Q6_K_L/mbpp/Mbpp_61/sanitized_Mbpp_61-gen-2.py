def count_Substrings(s):
    def sum_digits(s):
        return sum(int(c) for c in s)

    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if sum_digits(substr) == len(substr):
                count += 1
    return count