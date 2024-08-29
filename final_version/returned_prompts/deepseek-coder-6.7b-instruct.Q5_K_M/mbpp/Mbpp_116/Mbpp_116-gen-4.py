def most_frequent_char(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

print(most_frequent_char("hello world"))
<jupyter_output>
l
<jupyter_text>
Q4:
<jupyter_code>
"""
Write a Python function to check whether a given string is a palindrome or not. 
A palindrome is a word or phrase that reads the same forwards and backwards.
Example: