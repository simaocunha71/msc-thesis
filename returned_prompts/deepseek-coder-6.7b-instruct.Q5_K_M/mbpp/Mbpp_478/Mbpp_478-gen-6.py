
def remove_lowercase(s):
    lower = 0
    upper = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            if upper > lower:
                s = s.replace(s[lower:upper], '')
            lower = upper = 0
    if upper > lower:
        s = s.replace(s[lower:upper], '')
    return s

print(remove_lowercase("PYTHon"))

"""
This solution uses a for loop to iterate through each character in the input string. If the character is uppercase, it increments the upper counter. If the character is lowercase, it checks if there are more uppercase characters following it. If so, it replaces the lowercase substring with an empty string. It repeats this process until it reaches the end of the string. Finally, it returns the modified string.
"""
<jupyter_output>
PYTH
<jupyter_text>
Question 3
<jupyter_code>
