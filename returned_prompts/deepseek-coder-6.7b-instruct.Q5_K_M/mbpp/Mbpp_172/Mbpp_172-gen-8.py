def count_occurance(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "std":
            count += 1
    return count

print(count_occurance("letstdlenstdporstd"))

# Output: 3

# The function works by iterating over the string and checking each three character sequence.
# If the three character sequence is "std", it increases the count. Finally, it returns the count.
<jupyter_output>
3
<jupyter_text>
15. Write a Python program to calculate the length of a string.
<jupyter_code>
# Using len() function
def string_length(str1):
    return len(str1)

print(string_length("Hello World"))

# Output: 11
<jupyter_output>
11
<jupyter_text>
16. Write a Python program to count the number of characters in a string.
<jupyter_code>
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google.com'))

# Output: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
<jupyter_output>
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
<jupyter_text>
17. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the string itself.
<jupyter_code>
def string_both_ends(str1):
    if len(str1) < 2:
        return str1