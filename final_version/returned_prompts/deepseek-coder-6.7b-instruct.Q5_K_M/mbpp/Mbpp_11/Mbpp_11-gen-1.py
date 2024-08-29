
def remove_Occ(s, c):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c:
            s[i] = ''
            break
    for i in reversed(range(len(s))):
        if s[i] == c:
            s[i] = ''
            break
    return ''.join(s)

print(remove_Occ("hello","l"))

"""
This function works by converting the input string to a list, then iterating over the list from left to right and right to left. It first removes the first occurrence of the character and then the last occurrence. It then joins the list back into a string and returns it.
"""
<jupyter_output>
heo
<jupyter_text>
Q.2
<jupyter_code>
