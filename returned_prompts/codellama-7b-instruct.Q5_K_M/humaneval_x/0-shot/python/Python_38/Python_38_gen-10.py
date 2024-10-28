

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    return "".join(groups)


def test_encode_cyclic():
    assert encode_cyclic("abc") == "abc"
    assert encode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcdc") == "abcdc"
    assert encode_cyclic("abcdefg") == "abcdefg"
    assert encode_cyclic("abcdefgh") == "abcdefgh"
    assert encode_cyclic("abcdefghi") == "abcdefghi"
    assert encode_cyclic("abcdefghij") == "abcdefghij"
    assert encode_cyclic("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"


def test_decode_cyclic():
    assert decode_cyclic("abc") == "abc"
    assert decode_cyclic("abcd") == "abcd"
    assert decode_cyclic("abcdc") == "abcdc"
    assert decode_cyclic("abcdefg") == "abcdefg"
    assert decode_cyclic("abcdefgh") == "abcdefgh"
    assert decode_cyclic("abcdefghi") == "abcdefghi"
    assert decode_cyclic("abcdefghij") == "abcdefghij"
    assert decode_cyclic("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
