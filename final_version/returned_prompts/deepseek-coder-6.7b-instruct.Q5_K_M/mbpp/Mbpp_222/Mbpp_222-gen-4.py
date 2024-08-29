
def check_type(t):
    type_check = type(t[0])
    for i in t[1:]:
        if type(i) != type_check:
            return False
    return True

print(check_type((5, 6, 7, 3, 5, 6)))
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
