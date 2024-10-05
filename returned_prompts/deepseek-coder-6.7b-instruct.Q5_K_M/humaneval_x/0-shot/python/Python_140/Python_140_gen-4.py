
def fix_spaces(text):
    new_text = []
    count = 0
    for ch in text:
        if ch == ' ':
            count += 1
            if count == 2:
                new_text.append('_')
            elif count > 2:
                new_text[-1] = '-'
        else:
            if count > 1:
                new_text.append('_')
            count = 0
            new_text.append(ch)
    return ''.join(new_text)

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))
<jupyter_output>
Example
Example_1
_Example_2
_Example-3
<jupyter_text>
**Question 2**
<jupyter_code>
