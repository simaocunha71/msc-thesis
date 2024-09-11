"""
def first_repeated_char(s):
    char_set = set()
    for c in s:
        if c in char_set:
            return c
        else:
            char_set.add(c)
    return None

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    print("Passed")

if __name__ == "__main__":
    test_first_repeated_char()
"""

def first_repeated_char(s):
    char_set = set()
    for c in s:
        if c in char_set:
            return c
        else:
            char_set.add(c)
    return None

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    print("Passed")

if __name__ == "__main__":
    test_first_repeated_char()


def first_repeated_char(s):
    for c in s:
        if s.count(c) > 1 and s.index(c) == s.index(c, s.index(c)+1):
            return c
    return None

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    print("Passed")

if __name__ == "__main__":
    test_first_repeated_char()


def first_repeated_char(s):
    for c in s:
        if s.index(c) != s.index(c, s.index(c)+1):
            continue
        return c
    return None

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    print("Passed")

if __name__ == "__main__":
    test_first_repeated_char()


def first_repeated_char(s):
    d = {}
    for c in s:
        if c in d:
            return c
        else:
            d[c