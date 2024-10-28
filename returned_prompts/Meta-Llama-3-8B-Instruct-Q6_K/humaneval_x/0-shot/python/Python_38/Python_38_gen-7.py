```
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
    decoded_groups = []
    i = 0
    while i < len(s):
        if len(s) - i >= 3:
            group = s[i:i+3]
            decoded_groups.append(group[1:] + group[0])
            i += 3
        else:
            decoded_groups.append(s[i:])
            break
    return "".join(decoded_groups)
```
The encode_cyclic function works by splitting the input string into groups of three characters each. If a group has only two characters, it is left as is. Otherwise, it is cycled by moving the first character to the end of the group. The groups are then joined together to form the encoded string.

The decode_cyclic function works by reversing the process of encode_cyclic. It splits the input string into groups of three characters each, but instead of cycling the groups, it moves the first character of each group to the end of the group. The groups are then joined together to form the decoded string. If the input string has fewer than three characters, the remaining characters are returned as is.