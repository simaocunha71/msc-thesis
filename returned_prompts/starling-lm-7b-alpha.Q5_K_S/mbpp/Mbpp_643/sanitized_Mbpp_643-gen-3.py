import unittest
def text_match_wordz_middle(text):
    if 'z' in text:
        return text[0] != 'z' and text[-1] != 'z'
    else:
        return False