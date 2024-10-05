    return "".join([chr(((ord(ch) - ord("a")) % 26) + ord("a")) for ch in s])
# decode_shift(encode_shift("hello")) should return "hello"  # Test case


