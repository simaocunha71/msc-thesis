def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count