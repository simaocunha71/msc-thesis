def toggle_string(s):
    return s.swapcase()

print(toggle_string("Python"))

#Alternate solution
def toggle_string(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

print(toggle_toggle_string("Python"))
<jupyter_output>
pYTHON
pYTHON
<jupyter_text>
Question 2
<jupyter_code>
