

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
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def test_cyclic_encoding(s: str, expected: str):
    assert encode_cyclic(s) == expected


def test_cyclic_decoding(s: str, expected: str):
    assert decode_cyclic(encode_cyclic(s)) == s
