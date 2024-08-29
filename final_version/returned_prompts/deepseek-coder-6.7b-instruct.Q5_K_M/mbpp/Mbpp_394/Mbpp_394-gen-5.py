
def check_distinct(t):
    if len(t) == len(set(t)):
        return True
    else:
        return False

print(check_distinct((1, 4, 5, 6, 1, 4)))
<jupyter_output>
False
<jupyter_text>
Q2.Write a function that takes a list of strings and returns the string with the most characters.
<jupyter_code>
