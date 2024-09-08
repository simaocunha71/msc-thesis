def count_Substrings(s: str) -> int:
    n = len(s)
    count = 0
    for length in range(1, n+1):
        for i in range(n-length+1):
            substring = s[i:i+length]
            if sum(int(digit) for digit in substring) == length:
                count += 1
    return count

# Test the function
assert count_Substrings('112112') == 6
"""
The substrings are:
1
1
2
1
1
2
11
12
21
112
121
211
122
11
2
1
"""

# Explanation: The substrings are '1', '1', '2', '1', '1', '2', '11', '12', '21', '112', '121', '211', '122', '11' and '2'. All of them have their sum of digits equal to their length except '21' which has sum of digits 3 which is not equal to its length.
<jupyter_output>
<empty_output>
<jupyter_text>
