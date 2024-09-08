def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)

print(replace_char("polygon",'y','l'))

# Output:
# polygon
# pollgon

# This is because the replace() function in Python replaces the old character with the new character in the given string and returns the new string.

# Note: If you want to replace the characters in the original string itself, you should pass the string as a list in the replace() function, like this: return list(s).replace(old_char, new_char).
# Please note that this will return a list, so you would need to join it back into a string with "".join(list) if you want to return a string.
<jupyter_output>
polygon
pollgon
<jupyter_text>
Question 2:Write a function that counts the number of occurrences of a substring in a given string.
<jupyter_code>
