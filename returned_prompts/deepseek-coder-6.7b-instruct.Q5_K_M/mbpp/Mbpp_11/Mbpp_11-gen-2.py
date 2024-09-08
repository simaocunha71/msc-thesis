def remove_Occ(s, c):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c:
            s[i] = ''
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] == c:
            s[i] = ''
            break
    return ''.join(s)

print(remove_Occ("hello", "l"))

"""
The function works by converting the string into a list of characters, then iterating through the list.
When it finds the first occurrence of the character to be removed, it replaces it with an empty string and breaks the loop.
It then does the same in reverse, but this time starting from the end of the list.
Finally, it joins the list back together into a string and returns the result.
"""
<jupyter_output>
heo
<jupyter_text>
Exercise 2
<jupyter_code>
