"""
def first_repeated_char(s):
    seen_chars = set()
    for c in s:
        if c in seen_chars:
            return c
        seen_chars.add(c)
    return None


def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"


test_first_repeated_char()
"""

def first_repeated_char(s):
    seen_chars = set()
    for c in s:
        if c in seen_chars:
            return c
        seen_chars.add(c)
    return None


def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"


test_first_repeated_char()



"""

