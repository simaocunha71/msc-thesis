def first_repeated_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abcd") == None
assert first_repeated_char("abcabcabcabc") == "a"
assert first_repeated_char("aaaaa") == "a"
assert first_repeated_char("") == None

"""
