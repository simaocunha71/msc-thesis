
    # split string to groups. Each of length 3.
    groups ​​= ​​[​​s​​[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups ​​= ​​[​​(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


if __name__ == "____main__":
    test_string = "abcdefghijklmnopqrstuvwxyz1234567890"
    encoded_string = encode_cyclic(test_string)
    decoded_string = decode_cyclic(encoded_string)
    print(f"Test String: {test_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
    assert test_string == decoded_string, "encoding and decoding failed"

#tests/test_cyclic_encode_decode.py
import pytest
from cyclic_encode_decode import encode_cyclic, decode_cyclic


def test_cyclic_encode_decode():
    test_string = "abcdefghijklmnopqrstuvwxyz1234567890"
    encoded_string = encode_cyclic(test_string)
    decoded_string = decode_cyclic(encoded_string)
    assert test_string == decoded_string, "encoding and decoding failed"


def test_cyclic_encode_decode_empty():
    test_string = ""
    encoded_string = encode_cyclic(test_string)
    decoded_string = decode_cyclic(encoded_string)
    assert test_string == decoded_string, "encoding and decoding failed"


def test_cyclic_encode_decode_single_char():
    test_string = "a