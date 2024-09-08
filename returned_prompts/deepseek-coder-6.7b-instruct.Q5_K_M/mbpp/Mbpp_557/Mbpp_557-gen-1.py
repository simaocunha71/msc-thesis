
def toggle_string(s):
    return s.swapcase()

print(toggle_string("Python"))

# Alternatively
def toggle_string(s):
    res = ""
    for char in s:
        if char.isupper():
            res += char.lower()
        else:
            res += char.upper()
    return res

print(toggle_toggle_string_string("Python"))

#Alternatively
def toggle_string(s):
    return ''.join(char.upper() if char.islower() else char.lower() for char in s)

print(toggle_string("Python"))

#Alternatively
def toggle_string(s):
    return ''.join([char.upper() if char.islower() else char.lower() for char in s])

print(toggle_string("Python"))

#Alternatively
def toggle_string(s):
    return ''.join(map(lambda c: c.upper() if c.islower() else c.lower(), s))

print(toggle_string("Python"))
<jupyter_output>
pYTHON
pYTHON
pYTHON
pYTHON
pYTHON
<jupyter_text>
Question 3:Write a Python function to replace all occurrences of a substring in a string with another substring.
<jupyter_code>
