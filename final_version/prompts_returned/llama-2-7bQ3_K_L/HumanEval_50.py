

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr((ord(ch) - 5 + ord("a")) % 26) for ch in s])

def encode_rot13(s: str):
    # Rotation of 13 means the shift is (-13, 13), or (26, -19). 
    """
    returns encoded string by rotating the input by 13 places to the left.
    """
    return "".join([chr((ord(ch) + ord("z")) % 26) for ch in s])


def decode_rot13(s: str):
    # Rotation of 13 means the shift is (-13, 13), or (26, -19). 
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr((ord(ch) - ord("z")) % 26) for ch in s])