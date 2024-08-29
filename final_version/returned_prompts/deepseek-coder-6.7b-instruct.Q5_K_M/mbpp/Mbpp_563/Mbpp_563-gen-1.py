
def check_special_characters(s):
    import re
    return bool(re.search(r'\W', s))

print(check_special_characters('data science is fun 123 and 45.67'))
print(check_special_characters('data$cience#is@fun'))
<jupyter_output>
False
True
<jupyter_text>
Q4:
<jupyter_code>
"""
Write a function to validate if a string is a valid email address.
assert validate_email('test@gmail.com')==True
assert validate_email('