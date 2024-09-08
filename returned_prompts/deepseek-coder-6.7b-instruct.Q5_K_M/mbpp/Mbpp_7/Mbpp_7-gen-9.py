def find_char_long(s):
    return [word for word in s.split() if len(word) >= 4]

print(set(find_char_long('Please move back to stream')))

# or

def find_char_long(s):
    return list(filter(lambda word: len(word) >= 4, s.split()))

print(set(find_char_long('Please move back to stream')))

# or

import re

def find_char_long(s):
    return re.findall(r'\b\w{4,}\b', s)

print(set(find_char_long('Please move back to stream')))

# all of them will give the same output:
# {'stream', 'Please', 'move', 'back'}
<jupyter_output>
{'stream', 'Please', 'move', 'back'}
{'stream', 'Please', 'move', 'back'}
{'stream', 'Please', 'move', 'back'}
<jupyter_text>
