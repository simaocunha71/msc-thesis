def count_Substrings(s):
    n = len(s)
    count = 0
    for length in range(1, n+1):
        for start in range(n-length+1):
            end = start + length
            if sum(int(x) for x in s[start:end]) == length:
                count += 1
    return count

print(count_Substrings('112112'))

Explanation:
This code works by iterating over all possible substrings of the given string, and for each one, it calculates the sum of the digits in the substring and checks if it equals the length of the substring. If they are equal, it increments the count. Finally, it returns the count.
"""

# 2nd Solution:
"""
