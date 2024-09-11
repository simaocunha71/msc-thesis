"""
def text_starta_endb(s):
    return s[0] == 'a' and s[-1] == 'b'

def test_starta_endb():
    assert text_starta_endb("aabbbb") == True
    assert text_starta_endb("aaabbb") == False
    assert text_starta_endb("axb") == False
    assert text_starta_endb("axbb") == True
    assert text_starta_endb("ax") == False

test_starta_endb()
"""

def text_starta_endb(s):
    return s.startswith('a') and s.endswith('b')

def test_starta_endb():
    assert text_starta_endb("aabbbb") == True
    assert text_starta_endb("aaabbb") == False
    assert text_starta_endb("axb") == False
    assert text_starta_endb("axbb") == True
    assert text_starta_endb("ax") == False

test_starta_endb()

# Another solution using a function that only checks for the 'a' and 'b' conditions separately
def text_starta_endb(s):
    return s.startswith('a') and s.endswith('b')

def test_starta_endb():
    assert text_starta_endb("aabbbb") == True
    assert text_starta_endb("aaabbb") == False
    assert text_starta_endb("axb") == False
    assert text_starta_endb("axbb") == True
    assert text_starta_endb("ax") == False

test_starta_endb()

# Another solution using a function that only checks for the 'a' and 'b' conditions separately
def text_starta_endb(s):
    return s.startswith('a') and s.endswith('b')

def test_starta_endb():
    assert text_starta_endb("aabbbb")