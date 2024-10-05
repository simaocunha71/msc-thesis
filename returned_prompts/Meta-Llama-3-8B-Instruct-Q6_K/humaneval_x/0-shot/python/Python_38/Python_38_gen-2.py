```
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    encoded = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            encoded += group[1:] + group[0]
        else:
            encoded += group
    return encoded

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    decoded = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            decoded += group[2] + group[0] + group[1]
        else:
            decoded += group
    return decoded
```



The encode_cyclic function splits the input string into groups of 3 characters. If a group has fewer than 3 characters, it is left as is. Otherwise, the first and third characters are swapped. The function then joins these groups together to form the encoded string.

The decode_cyclic function does the opposite. It splits the encoded string into groups of 3 characters. If a group has fewer than 3 characters, it is left as is. Otherwise, the first and third characters are swapped, and the second character is moved to the first position. The function then joins these groups together to form the decoded string.

These functions can be used together to create a simple form of encryption and decryption. The encode_cyclic function can be used to encode a string, and the decode_cyclic function can be used to decode it.