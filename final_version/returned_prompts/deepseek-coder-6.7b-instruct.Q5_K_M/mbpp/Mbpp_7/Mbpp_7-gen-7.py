def find_char_long(s):
    return [i for i in s.split() if len(i) >= 4]

print(set(find_char_long('Please move back to stream')))
<jupyter_output>
{'Please', 'move', 'stream', 'back'}
<jupyter_text>
