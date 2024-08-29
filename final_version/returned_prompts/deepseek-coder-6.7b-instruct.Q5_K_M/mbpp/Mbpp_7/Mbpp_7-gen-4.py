def find_char_long(string):
    return [word for word in string.split() if len(word) >= 4]

print(set(find_char_long('Please move back to stream')))

#Output: {'move', 'stream', 'Please', 'back'}

#Answer:
def find_char_long(s):
    return [word for word in s.split() if len(word)>=4]

assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
