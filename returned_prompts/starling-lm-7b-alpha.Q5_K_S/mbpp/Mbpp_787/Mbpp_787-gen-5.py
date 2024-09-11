"""
def text_match_three(string):
    """
    Returns True if the string has an a followed by three b's, and False otherwise.
    """
    if len(string) < 3:
        return False
    if string[0] == 'a' and string[1:4] == 'bbb':
        return True
    else:
        return False

def test_text_match_three():
    assert not text_match_three("ac")
    assert text_match_three("abbb")
    assert not text_match_three("abc")
    assert not text_match_three("ab")
    assert not text_match_three("axaxaa")
    assert not text_match_three("axaaaxaxaa")
    assert text_match_three("aybbayyaaayayayayayayayayayayayyaayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay