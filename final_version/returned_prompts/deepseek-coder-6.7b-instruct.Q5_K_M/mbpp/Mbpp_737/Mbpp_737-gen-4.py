
import re

def check_str(s):
    return bool(re.match(r'^[aeiou]', s))

print(check_named_entity("annie"))

"""
This script uses the `re.match()` function to check if the given string starts with a vowel. 
The regex pattern `^[aeiou]` matches any string that starts with a vowel (a, e, i, o, u). 
The `bool()` function is used to convert the match object to a boolean value. 
If the string starts with a vowel, the function will return True; otherwise, it will return False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a python program to find the square root of a number using regex.
<jupyter_code>
