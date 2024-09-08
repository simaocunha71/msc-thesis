
def number_ctr(s):
    ctr = 0
    for i in s:
        if i.isdigit():
            ctr += 1
    return ctr

assert number_ctr('program2bedone') == 1
assert number_ctr('123456789') == 9
assert number_ctr('abcdefgh') == 0
assert number_ctr('') == 0
assert number_ctr('111111111') == 9
assert number_ctr('program2bedone3') == 2

print("All tests passed.")

"""
In this function, we use a for loop to iterate over each character in the string. The isdigit() method is used to check if the character is a digit. If it is, we increment our counter by 1. Finally, we return the counter.
"""
<jupyter_output>
All tests passed.
<jupyter_text>
Question 2
<jupyter_code>
