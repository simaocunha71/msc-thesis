def encode_cyclic(s):
    """ returns encoded string by cycling groups of three characters. """
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            groups[i] = groups[i][1:] + groups[i][0]
    return ''.join(groups)


def decode_cyclic(s):
    """ takes as input string encoded with encode_cyclic function. Returns decoded string. """
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    for i in range(len(groups)):
        if len(groups[i]) == 3:
            groups[i] = groups[i][-1] + groups[i][:-1]
    return ''.join(groups)