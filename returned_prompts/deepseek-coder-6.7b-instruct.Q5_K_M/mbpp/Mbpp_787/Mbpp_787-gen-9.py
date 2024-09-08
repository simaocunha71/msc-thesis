"""
import re

def text_match_three(text):
    patterns = 'ab{3}'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match_three("abbb"))
print(text_match_three("ac"))
"""

