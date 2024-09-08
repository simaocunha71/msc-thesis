def find_char_long(string):
    return [word for word in string.split() if len(word) >= 4]

print(set(find_char_long('Please move back to stream')))
<jupyter_output>
{'move', 'stream', 'Please', 'back'}
<jupyter_text>
Question 2
<jupyter_code>
