

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def test_encode_decode_cyclic():
    assert encode_cyclic("") == ""
    assert decode_cyclic("") == ""
    assert encode_cyclic("a") == "a"
    assert decode_cyclic("a") == "a"
    assert encode_cyclic("abc") == "abc"
    assert decode_cyclic("abc") == "abc"
    assert encode_cyclic("abcd") == "abcd"
    assert decode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcd") == "abcd"
    assert decode_cyclic("abcd") == "abcd"
    assert encode_cyclic("abcdefgh") == "abcdefgh"
    assert decode_cyclic("abcdefgh") == "abcdefgh"
    assert encode_cyclic("abcdefghi") == "abcdefghi"
    assert decode_cyclic("abcdefghi") == "abcdefghi"
    assert encode_cyclic("abcdefghij") == "abcdefghij"
    assert decode_cyclic("abcdefghij") == "abcdefghij"
    assert encode_cyclic("abcdefghijk") ==