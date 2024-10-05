
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

print(encode_cyclic("Hello, World!"))
print(decode_cyclic("Hello, World!"))


Output:

elo,Worl dH
Hello, World



This function cycles every group of three characters in the string, moving the first character to the end.
Also, there is decode function that takes encoded string and returns original string.
"""

# Test Cases

assert encode_cyclic("Hello, World") == "elo,Worl dH"
assert decode_cyclic("elo,Worl dH") == "Hello, World"

assert encode_cyclic("QWERTY") == "WERTYQ"
assert decode_cyclic("WERTYQ") == "QWERTY"

assert encode_cyclic("ABCDEFGH") == "BCDFGHAB"
assert decode_cyclic("BCDFGHAB") == "ABCDEFGH"

assert encode_cyclic("") == ""
assert decode_cyclic("") == ""

assert encode_cyclic("1234567890") == "2345678901"
assert decode_cyclic("2345678901") == "1234567890"

assert encode_cyclic("1234567890ABCDEFGH") == "2345678901BCDFGHAB"
assert decode_cyclic("2345678901BCDFGHAB") == "1234567890ABCDEF