

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    return "".join(s[i:i + 3] for i in range(0, len(s), 3))


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """

B:


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    return "".join(s[i:i + 3] for i in range(0, len(s), 3))


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    return "".join(groups)

C:


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    return "".join(s[i:i + 3] for i in range(0, len(s), 3))


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    groups = [(groups[1:] + groups[0]) if len(groups) == 3 else groups for groups in groups]
    return "".join(groups)

D:


def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    return "".join(s[i:i + 3] for i in range(0, len(s), 3))


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
