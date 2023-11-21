

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups of three characters each.
    chars = "".join([s[(3 * i):min((3 * i + 3), len(s))] for i in range(0, len(s) // 3 + (len(s) % 3 == 2))])
    # join groups of three characters each.
    return "".join([chars[i:] + chars[:3] if len(chars[i:]) == 3 else chars for i in range((len(chars) - 1) // 3)])

if __name__ == '__main__':
    # test encoded string.
    enc = encode_cyclic("abcdefg")
    dec = decode_cyclic(enc)
    print(enc, dec)