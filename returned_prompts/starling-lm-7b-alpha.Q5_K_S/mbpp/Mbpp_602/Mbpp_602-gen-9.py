"""
def first_repeated_char(s):
    seen = {}
    for c in s:
        if c in seen:
            return c
        seen[c] = True
    return None

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    print("All tests passed.")

test_first_repeated_char()
"""

