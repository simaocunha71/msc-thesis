def count_Substrings(s):
    cnt = 0
    for length in range(1, len(s) + 1):
        for start in range(0, len(s) - length + 1):
            substr = s[start:start + length]
            if sum(int(ch) for ch in substr) == length:
                cnt += 1
    return cnt

print(count_Substrings('112112'))

"""
Here is the explanation of the code:

1. We initialize a counter variable to 0.
2. We iterate over each possible length of substring from 1 to the length of the string.
3. For each possible length, we iterate over each possible starting index of the substring within the range of the string length minus the length of the substring plus 1.
4. For each possible starting index, we create a substring of the desired length.
5. We then check if the sum of the digits of the substring is equal to its length. If it is, we increment the counter.
6. Finally, we return the counter.
"""

"""
This solution works in O(n^2) time complexity where n is the length of the string. This is because we have two nested loops, each going up to n iterations. This makes the function perform well for strings of reasonable length. The space complexity is O(n) because we create substrings of the string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
