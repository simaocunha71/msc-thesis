
def text_match_two_three(text):
    import re
    pattern = 'ab{2,3}'
    if re.search(pattern, text):
        return True
    else:
        return False

print(text_match_two_three("ac"))

# Expected Output: False
<jupyter_output>
False
<jupyter_text>
Question 2:
<jupyter_code>
