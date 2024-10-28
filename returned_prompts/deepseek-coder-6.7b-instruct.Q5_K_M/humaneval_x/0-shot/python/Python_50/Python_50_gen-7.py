

def decode_shift(s: str):
    """
    returns decoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


print(encode_shift("hello"))
print(decode_shift(encode_shift("hello")))

#test/test_encode_decode.py
import pytest
from solution import encode_shift, decode_shift


def test_encode_shift():
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("world") == "zwygp"
    assert encode_shift("code") == "hqfr"
    assert encode_shift("python") == "trnqlw"


def test_decode_shift():
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("zwygp") == "world"
    assert decode_shift("hqfr") == "code"
    assert decode_shift("trnqlw") == "python"


def test_encode_decode_shift():
    test_strings = ["hello", "world", "code", "python"]
    for s in test_strings:
        assert decode_shift(encode_shift(s)) == s


if __name__ == "__main__":
    pytest.main(["-v", __file__])

#test/test_encode_shift.py
import pytest
from solution import encode_shift


def test_encode_shift():
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("world") == "zwygp"
    assert encode_shift("code") == "hqfr"
    assert encode_shift("python") == "trnqlw"


if __name__ == "__main__":
    pytest.main(["-v", __file__])

#test/test_functions.py
import pytest
from solution import encode_shift, decode_shift

