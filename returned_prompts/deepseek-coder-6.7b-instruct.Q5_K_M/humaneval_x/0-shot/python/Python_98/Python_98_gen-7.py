
    vowels = 'AEIOU'
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)

print(count_upper('aBCdEf'))  # 1
print(count_upper('abcdefg'))  # 0
print(count_upper('dBBE'))  # 0
print(count_upper('ABCDE'))  # 3
print(count_upper('bcdfg'))  # 0
print(count_upper('ABCDEFG'))  # 2
print(count_upper('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'))  # 12
<jupyter_output>
1
0
0
3
0
2
12
<jupyter_text>
Problem 2 - Count LowerCase Vowels in Odd Indices (25 pts)Write a function `count_lower` that counts the number of lowercase vowels in odd indices of a given string. Your function should return the count.For example:`count_lower('aBCdEf')` returns 1`count_lower('abcdefg')` returns 0`count_lower('dBBE')` returns 0`count_lower('ABCDE')` returns 0`count_lower('bcdfg')` returns 1`count_lower('ABCDEFG')` returns 1`count_lower('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ')` returns 6
<jupyter_code>
def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 1
    count_lower('abcdefg') returns 0
    count_lower('dBBE') returns 0
    count_lower('ABC