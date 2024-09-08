
def check_type(tup):
    type_check = type(tup[0])
    for i in tup[1:]:
        if type(i) != type_check:
            return False
    return True

print(check_type((5, 6, 7, 3, 5, 6)))
print(check_type((5, 6, '7', 3, 5, 6)))
<jupyter_output>
True
False
<jupyter_text>
Question 2:
<jupyter_code>
