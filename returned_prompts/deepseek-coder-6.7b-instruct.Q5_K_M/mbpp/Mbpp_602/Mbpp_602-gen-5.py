def first_repeated_char(s: str):
    chars = set()
    for char in s:
        if char in chars:
            return char
        chars.add(char)
    return None

assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abcdef") == None
assert first_repeated_char("abac") == "a"
assert first_repeated_char("aabbc") == "a"
assert first_repeated_char("abcb") == "b"
assert first_repeated_char("abcdabcdefghijklmnopqrstuvwxyz") == None
assert first_repeated_char("aaab") == "a"
assert first_repeated_char("abab") == "a"
assert first_repeated_char("abcdabcd") == "a"
assert first_repeated_char("abcdabcdefghijklmnopqrstuvwxyz") == None
assert first_repeated_char("12345678901234567890") == None
assert first_repeated_char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == None
assert first_repeated_char("") == None
assert first_repeated_char("a") == None
assert first_repeated_char("aa") == "a"
assert first_repeated_char("ab") == None
assert first_repeated_char("ba") == None
assert first_repeated_char("abc") == None
assert first_repeated_char("bca") == None
assert first_repeated_char("123") == None
assert first_repeated_char("111") == "1"
assert first_repeated_char("123123") == "1"
assert first_repeated_char("abcdefghijklmnopqrstuvwxyz123") == None
assert first_re