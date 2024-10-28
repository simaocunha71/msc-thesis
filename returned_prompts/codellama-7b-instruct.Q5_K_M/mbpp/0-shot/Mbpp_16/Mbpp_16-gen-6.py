"""
import re

def text_lowercase_underscore(text):
    pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    return bool(pattern.match(text))
"""
