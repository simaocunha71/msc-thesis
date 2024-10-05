```python
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
    i = 0
    while i < len(s):
        if i + 2 < len(s):
            decoded += s[i+1] + s[i] + s[i+2]
            i += 3
        else:
            decoded += s[i:] + s[:i]
            break
    return decoded
```


The idea behind these functions is to cycle groups of three characters in the string. In the encode function, we split the string into groups of three characters, and then cycle the elements in each group. If a group has fewer elements than three, we leave it as it is. In the decode function, we iterate over the string, and whenever we find a group of three characters, we cycle them. If we don't find a group of three characters, we just append the remaining characters to the decoded string. This way, we effectively decode the cyclically encoded string.