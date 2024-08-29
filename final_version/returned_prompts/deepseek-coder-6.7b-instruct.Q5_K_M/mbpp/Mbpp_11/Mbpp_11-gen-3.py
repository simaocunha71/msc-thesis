def remove_Occ(s, ch):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ch:
            s[i] = ''
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            s[i] = ''
            break
    return ''.join(s)

print(remove_Occ("hello","l"))

# Output: "heo"

# In the given string "hello", the first and last occurrence of 'l' is removed. 
# So the new string is "heo".

# Here, we first convert the string into list to be able to modify characters in-place. 
# We then iterate from the start and end of the string, removing the first and last occurrence of the character. 
# Finally, we join the list back into a string.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
