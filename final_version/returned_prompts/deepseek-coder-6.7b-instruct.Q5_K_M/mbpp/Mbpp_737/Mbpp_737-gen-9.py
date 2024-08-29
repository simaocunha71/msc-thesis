
def check_str(s):
    import re
    pattern = '^[aeiou]'
    if re.match(pattern, s):
        return True
    else:
        return False

print(check_str("annie"))
print(check_str("banana"))
<jupyter_output>
True
False
<jupyter_text>
Q2: Write a function to check whether the given string is ending with a vowel or not using regex.
<jupyter_code>
def check_str(s):
    import re
    pattern = '[aeiou]$'
    if re.search(pattern, s):
        return True
    else:
        return False

print(check_str("annie"))
print(check_str("banana"))
<jupyter_output>
True
True
<jupyter_text>
Q3: Write a function to check whether the given string is a valid email or not using regex.
<jupyter_code>
def validate_email(s):
    import re
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(pattern, s):
        return True
    else:
        return False

print(validate_email("annie@gmail.com"))
print(validate_email("annie.gmail.com"))
<jupyter_output>
True
False
<jupyter_text>
Q4: Write a function to find all occurrences of a pattern in a string using regex.
<jupyter_code>
def find_all(s, pattern):
    import re
    return [m.start() for m in re.finditer(pattern, s)]

print(find_all("The black cat climbed the black roof and ate the black apple", "black"))
<jupyter_output>
[4, 29]
<jupyter_text>
Q5: Write a function to replace all occurrences of a pattern in a string using regex.