def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            digit_sum = sum(int(digit) for digit in substring)
            if digit_sum == len(substring):
                count += 1
    return count