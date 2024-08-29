
def is_lower(s):
    return s.lower()

print(is_lower("InValid"))

# Output: 'invalid'

# Other Solution:

def is_lower(s):
    return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s])

print(is_lower("InValid"))

# Output: 'inValid'
<jupyter_output>
invalid
inValid
<jupyter_text>
Problem 2: Write a python function to capitalize the first and fourth characters of a string.
<jupyter_code>
def capitalize_chars(s):
    if len(s) > 3:
        return s[:3] + s[3].upper() + s[4:]
    return s

print(capitalize_chars("hello"))
print(capitalize_chars("hey"))
# Output:
# ellO
# hey
<jupyter_output>
ellO
hey
<jupyter_text>
Problem 3: Write a Python function to replace the spaces with a hyphen.
<jupyter_code>
def replace_spaces(s):
    return s.replace(" ", "-")

print(replace_spaces("This is a test string"))
# Output:
# This-is-a-test-string
<jupyter_output>
This-is-a-test-string
<jupyter_text>
Problem 4: Write a Python function to remove all the vowels from a string.
<jupyter_code>
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([c for c in s if c not in vowels])

print(remove_vowels("This is a test string"))
# Output:
# Ths s  tst strng
<jupyter_output>
Ths s  tst strng
<jupyter_text>
Problem 5: Write a Python function to count the number of