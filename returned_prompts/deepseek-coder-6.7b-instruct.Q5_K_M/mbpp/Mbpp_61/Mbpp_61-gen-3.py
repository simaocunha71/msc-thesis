def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum = 0
        for j in range(i, len(s)):
            sum += int(s[j])
            if sum == j - i + 1:
                count += 1
    return count

print(count_Substrings('112112'))  # 6

Explanation:
The function `count_Substrings` takes a string `s` as an argument and initializes a counter `count` to 0. It then iterates over the string `s` and for each character, it calculates the sum of the digits from the current position `i` to the end of the string. If the sum equals the length of the substring from `i` to `j` (inclusive), it increments the counter `count`. Finally, it returns the counter `count`.
"""

# 12.
"""
