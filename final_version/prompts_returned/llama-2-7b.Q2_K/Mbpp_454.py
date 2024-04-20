"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""

def text_match_wordz(text):
    if len(text)>0:
        for i in range(len(text)-2, -1, -1):
            for j in range(i+2, len(text), 2):
                if text[j]=='z':
                    return True