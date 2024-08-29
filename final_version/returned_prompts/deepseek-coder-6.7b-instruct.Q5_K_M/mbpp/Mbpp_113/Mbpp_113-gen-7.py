def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(check_integer("python")) # False
print(check_integer("123")) # True

"""
This function will try to convert the string to an integer. If it succeeds, then the string is an integer and the function returns True. If it fails (throws a ValueError), then the string is not an integer and the function returns False.
"""
<jupyter_output>
False
True
<jupyter_text>
Q3. Write a Python function to check if a string is a valid email address.
<jupyter_code>
import re

def check_email(email):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
print(check_email("user@domain.com")) # True
print(check_email("user.name@domain.com")) # True
print(check_email("user_name@domain.com")) # True
print(check_email("user.name.2020@domain.com")) # True
print(check_email("user@sub.domain.com")) # True
print(check_email("user#domain.com")) # False
print(check_email("user@domain")) # False
print(check_email("user@domain.c")) # False
print(check_email("user@domain.co.in")) # True
<jupyter_output>
True
True
True
True
True
False
False
False
True
<jupyter_text>
Q4. Write a Python function to convert a string to its equivalent camel case.
<jupyter_code>
def to_camel_case(s):
    s = s.split(' ')
    return ''.join(word.title() for word in s)

# Test case
print