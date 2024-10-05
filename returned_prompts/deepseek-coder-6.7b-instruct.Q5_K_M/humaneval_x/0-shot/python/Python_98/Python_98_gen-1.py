
def count_upper(s):
    vowels = "AEIOU"
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)

print(count_upper('aBCdEf'))  # returns 1
print(count_upper('abcdefg'))  # returns 0
print(count_upper('dBBE'))  # returns 0
print(count_upper('AABBE'))  # returns 2
print(count_upper('AABBEE'))  # returns 3
print(count_upper('BBE'))  # returns 0
print(count_upper('bbe'))  # returns 0
print(count_upper('AaBeEc'))  # returns 1
print(count_upper('ABCDE'))  # returns 2
print(count_upper('aAbBcCdDeE'))  # returns 2
<jupyter_output>
1
0
0
2
3
0
0
1
2
2
<jupyter_text>
Question 2 (5 points)Write a Python function called `sum_between` that takes three arguments: `lst`, `start`, and `end`. The function should return the sum of the numbers in `lst` that are between `start` and `end` (inclusive) and that are divisible by 3.If `lst` does not contain any numbers between `start` and `end` that are divisible by 3, the function should return 0.
<jupyter_code>
