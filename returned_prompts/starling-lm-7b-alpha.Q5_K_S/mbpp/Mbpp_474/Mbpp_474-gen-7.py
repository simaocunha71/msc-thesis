def replace_char(s, c1, c2):
    for i in range(len(s)):
        if s[i] == c1:
            s = s[:i] + c2 + s[i+1:]
    return s

def test_replace_char():
    assert replace_char("polygon",'y','l') == "pollgon"

test_replace_char()





"""
def replace_char(s, c1, c2):
    for i in range(len(s)):
        if s[i] == c1:
            s = s[:i] + c2 + s[i+1:]
    return s

def test_replace_char():
    assert replace_char("polygon",'y','l') == "pollgon"

test_replace_char()
"""




"""
def replace_char(s, c1, c2):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c1:
            s[i] = c2
    return ''.join(s)

def test_replace_char():
    assert replace_char("polygon",'y','l') == "pollgon"

test_replace_char()
"""

"""
def replace_char(s, c1, c2):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c1:
            s[i] = c2
    return ''.join(s)

def test_replace_char():
    assert replace_char("polygon",'y','l') == "pollgon"

test_replace_char()
"""



"""
def replace_char(s, c1, c2):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c1:
            s[i] = c2
    return ''.join(s)

def test_replace_char():
    assert replace_char("polygon",'y','l') == "pollgon"

test_replace