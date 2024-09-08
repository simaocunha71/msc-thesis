def remove_Occ(s, ch):
    return s[:s.find(ch)] + s[s.rfind(ch) + 1:]

print(remove_Occ("hello","l"))


"""
Here we use the find() and rfind() methods to find the positions of the first and last occurrence of the character. 
Then we remove these occurrences from the string by slicing.
"""
<jupyter_output>
heo
<jupyter_text>
