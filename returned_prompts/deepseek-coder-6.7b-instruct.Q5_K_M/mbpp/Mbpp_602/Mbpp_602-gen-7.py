def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_repeated_char("abcabc"))  # "a"

