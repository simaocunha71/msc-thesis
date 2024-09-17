def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count