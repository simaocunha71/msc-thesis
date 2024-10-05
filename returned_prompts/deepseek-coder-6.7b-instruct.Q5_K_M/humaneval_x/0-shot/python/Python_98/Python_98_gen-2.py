
    vowels = 'AEIOU'
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)


print(count_upper('aBCdEf'))  # returns 1
print(count_upper('abcdefg'))  # returns 0
print(count_upper('dBBE'))  # returns 0
print(count_upper('QWERTY'))  # returns 1
print(count_upper('ABCDEFGHIJKL'))  # returns 3
print(count_upper('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'))  # returns 13
print(count_upper('aAeEiIoOuU'))  # returns 5
<jupyter_output>
1
0
0
1
3
13
5
<jupyter_text>
3. Write a function that takes a list of integers and returns the sum of all elements that are greater than the average.
<jupyter_code>
