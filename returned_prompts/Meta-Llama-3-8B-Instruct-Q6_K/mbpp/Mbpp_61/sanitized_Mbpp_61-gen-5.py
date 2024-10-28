def count_Substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count