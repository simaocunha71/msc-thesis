def move_num(s):
    nums = ''
    letters = ''
    for i in s:
        if i.isnumeric():
            nums += i
        else:
            letters += i
    return letters+nums

print(move_num('I1love143you55three3000thousand'))

"""
This function works by iterating over the string, checking if each character is numeric. If it is, it adds it to the nums string; if not, it adds it to the letters string.
Finally, it returns the concatenation of letters and nums.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 12:
<jupyter_code>
