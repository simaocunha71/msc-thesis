"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""

def text_match_wordz_middle(text):
    if text[0:1].lower() == "z":
        return True
    else: 
        if text[-3:] == 'z':
            return False
        else:
            return True