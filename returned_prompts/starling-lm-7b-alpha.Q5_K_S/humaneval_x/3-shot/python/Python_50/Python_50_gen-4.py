    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def test_encode_shift():
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("python") == "zvyqox"
    assert encode_shift("") == ""


def test_decode_shift():
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("zvyqox") == "python"
    assert decode_shift("") == ""


