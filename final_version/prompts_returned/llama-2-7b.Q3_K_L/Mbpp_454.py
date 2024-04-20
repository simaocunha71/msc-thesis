"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
import re
def match_wordz(text):
    words = "".join([i for i in text.split(' ') if len(i)>0]).lower()
    if not words: return False
    wordz = ['z']
    # 1, find the position of a character
    start_matching = re.search("[a-zA-Z]",words)
    # if you don't find any match for [a-zA-Z], break it to return False
    if not start_matching: return False
    wordz.append(start_matching.group())  # add the matched character to words
    while re.search("[a-zA-Z]",words):
        match = re.search("[a-zA-Z]",words)
        if not match: break
        else: words += re.sub(match.group(),"",words)  # remove the matched character in words and replace it with "" to continue searching
    return True