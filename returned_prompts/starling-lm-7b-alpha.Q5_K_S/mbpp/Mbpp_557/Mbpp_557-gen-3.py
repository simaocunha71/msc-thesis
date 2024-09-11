def toggle_string(s):
    res = ""
    for c in s:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    assert toggle_string("hello") == "HELLO"
    assert toggle_string("stackoverflow") == "STACKOVERFLOW"


if __name__ == "__main__":
    test_toggle_string()


def toggle_string(s):
    return s.swapcase()


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    assert toggle_string("hello") == "HELLO"
    assert toggle_string("stackoverflow") == "STACKOVERFLOW"


if __name__ == "__main__":
    test_toggle_string()


def toggle_string(s):
    return s.swapcase()


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    assert toggle_string("hello") == "HELLO"
    assert toggle_string("stackoverflow") == "STACKOVERFLOW"


if __name__ == "__main__":
    test_toggle_string()


def toggle_string(s):
    return s.swapcase()


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
    assert toggle_string("hello") == "HELLO"
    assert toggle_string("stackoverflow") == "STACKOVERFLOW"


if __name__ == "__main__":
    test_toggle_string()


def toggle_string(s):
    res = ""
    for c in s:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res


def test_toggle_string():
    assert toggle_string("Python") == "pYTHON"
   