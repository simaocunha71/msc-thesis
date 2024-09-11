"""
def text_match_three(text):
    """
    Returns True if the string has an a followed by three 'b', and False otherwise.
    """
    if text.startswith('a'):
        return len(text) > 1 and text[1] == 'b' and text[2] == 'b' and text[3] == 'b'
    else:
        return False

# Tests
assert not text_match_three("ac")
assert text_match_three("abbb")
assert text_match_three("aba")
assert not text_match_three("ab")
assert not text_match_three("abc")

"""

