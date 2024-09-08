def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abc") == None
assert first_repeated_char("aabbcc") == "a"
assert first_repeated_char("abcd") == None
assert first_repeated_char("abcdefgabcdefg") == "a"
assert first_repeated_char("12345678901234567890") == "1"
assert first_repeated_char("abcdefgabcdefg") == "a"
assert first_repeated_char("111111111111") == "1"
assert first_repeated_char("aaa") == "a"
assert first_repeated_char("aba") == "a"
assert first_repeated_char("abcdefgabcdefg") == "a"
assert first_repeated_char("1234567890") == None
assert first_repeated_char("aaaaaaa") == "a"
assert first_repeated_char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "a"
assert first_repeated_char("12345678901234567890") == "1"
assert first_repeated_char("aaaaaaa") == "a"
assert first_repeated_char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "a"
assert first_repeated_char("1234567890") == None
assert first_repeated_char("aaaaaaa") == "a"
assert first_repeated_char("abcdefghijklmnopqrst