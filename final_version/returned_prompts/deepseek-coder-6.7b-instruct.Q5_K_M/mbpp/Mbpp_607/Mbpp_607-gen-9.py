
def split_string(string):
    return re.findall(r'\b\w+\b', string)

print(split_string('The quick brown fox jumps over the lazy dog.'))
<jupyter_output>
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
<jupyter_text>
Q4:
<jupyter_code>
"""
Write a function to find and return all matches of a regex pattern in a string. The function should take two arguments - the string to search