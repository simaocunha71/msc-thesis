
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

# Test cases:
print(count_upper('aBCdEf'))  # returns 1
print(count_upper('abcdefg'))  # returns 0
print(count_upper('dBBE'))  # returns 0
print(count_upper('ABCDE'))  # returns 3
print(count_upper(''))  # returns 0
print(count_upper('A'))  # returns 1
print(count_upper('b'))  # returns 0
print(count_upper('AB'))  # returns 1
print(count_upper('abcdef'))  # returns 0
print(count_upper('ABC'))  # returns 1
print(count_upper('aBcDeF'))  # returns 1
<jupyter_output>
1
0
0
3
0
1
0
1
0
1
<jupyter_text>
Question 2: Write a function to count the number of lowercase vowels in odd indices.
<jupyter_code>
