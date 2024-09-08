def count_Substrings(s):
    n = len(s)
    count = 0
    for length in range(1, n+1):
        for i in range(n-length+1):
            substring = s[i:i+length]
            if sum(int(digit) for digit in substring) == length:
                count += 1
    return count

print(count_Substrings('112112'))  # 6

Explanation:
The function works by iterating over all possible lengths of substrings from 1 to the length of the string. For each length, it iterates over all substrings of that length. It then checks if the sum of the digits in the substring is equal to the length of the substring. If it is, it increments the count. Finally, it returns the count.
"""
