```
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
    decoded_string = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            decoded_string += group[2] + group[0] + group[1]
        else:
            decoded_string += group
    return decoded_string
```
The `encode_cyclic` function splits the input string into groups of 3 characters each, cycles the elements in each group, and then joins the groups back together to form the encoded string.

The `decode_cyclic` function takes the encoded string and reverses the process. It splits the string into groups of 3 characters each, checks if each group has 3 characters, and if so, rearranges the characters to their original order. The decoded string is then returned. If a group has fewer than 3 characters, it is added to the decoded string as is, since it cannot be decoded further.