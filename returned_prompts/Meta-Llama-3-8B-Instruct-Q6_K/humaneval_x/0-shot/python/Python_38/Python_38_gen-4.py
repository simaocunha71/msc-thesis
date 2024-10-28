```
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups = [(group[2] + group[0] + group[1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups = [(group[1] + group[2] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```



Explanation:

The `encode_cyclic` function splits the input string `s` into groups of three characters each. If a group has fewer than three characters, it is left unchanged. Then, it cycles the elements in each group by moving the first character to the end of the group and concatenating the groups.

The `decode_cyclic` function does the opposite. It splits the input string into groups of three characters each. If a group has fewer than three characters, it is left unchanged. Then, it cycles the elements in each group by moving the first character to the end of the group and concatenating the groups.

The main difference between the two functions is the way they cycle the elements in each group. `encode_cyclic` moves the first character to the end of the group, while `decode_cyclic` moves the first character to the end of the group and then moves the second character to the beginning of the group. This is because the `encode_cyclic` function is designed to encode the string, while the `decode_cyclic` function is designed to decode the string.

For example, if the input string is "hello", the `encode_cyclic` function would return the string "holle". If the input string is "holle", the `decode_cyclic` function would return the original string "hello".