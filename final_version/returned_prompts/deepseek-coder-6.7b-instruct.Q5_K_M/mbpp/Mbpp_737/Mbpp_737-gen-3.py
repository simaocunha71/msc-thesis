
def check_str(s):
    import re
    return bool(re.match(r'^[aeiou]', s, re.I))

print(check_srt("annie"))

"""
The function check_str uses regex to match the string. The ^ symbol specifies start of the line, [aeiou] specifies any character in the set {a, e, i, o, u}, and re.I makes the match case insensitive.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3: Write a Python program to check if the given input is valid e-mail address.
<jupyter_code>
