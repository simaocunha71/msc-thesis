
def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

print(count_upper('aBCdEf'))  # returns 1
print(count_upper('abcdefg'))  # returns 0
print(count_upper('dBBE'))  # returns 0
print(count_upper('ABCDEF'))  # returns 3
print(count_upper('ABC'))  # returns 1

# Explanation:
# In 'aBCdEf', 'B' and 'E' are the characters at even indices, and 'B' and 'E' are uppercase vowels.
# In 'abcdefg', there are no uppercase vowels in even indices.
# In 'dBBE', 'B' and 'E' are the characters at even indices, and 'B' and 'E' are uppercase vowels.
# In 'ABCDEF', 'A', 'E', 'C' are the uppercase vowels at even indices.
# In 'ABC', 'A' is the uppercase vowel at even index.

# The function traverses the string from the start to the end with a step of 2 (thus getting only the characters at even indices), and for each of those characters, if it is uppercase and a vowel, it increments the count. The final count is then returned.
<jupyter_output>
1
0
0
3
1
<jupyter_text>
Q2: Write a Python function that takes a list of numbers and returns a dictionary with keys being the unique numbers in the list, and values being the count of their occurrences in the list.For example:count_numbers([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) should return {1: 1, 2: 2, 3: 3, 4: 4}
<jupyter_code>
def count_numbers(lst):
    count_dict = {}
    for num in lst:
        if num in