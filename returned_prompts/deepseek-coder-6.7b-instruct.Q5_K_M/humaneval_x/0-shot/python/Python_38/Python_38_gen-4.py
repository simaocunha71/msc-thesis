
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group back to original position. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


if __name__ == "____main__":
    test_str = "Hello World!"
    encoded_str = encode_cyclic(test_str)
    print(f"Encoded: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded: {decoded_str}")
<jupyter_output>
Encoded: eHlloWorlld
Decoded: Hello World
<jupyter_text>
Task 2: Write a function, which takes as input a string and returns a string where each character is replaced by its ordinal position in the string.
<jupyter_code>
