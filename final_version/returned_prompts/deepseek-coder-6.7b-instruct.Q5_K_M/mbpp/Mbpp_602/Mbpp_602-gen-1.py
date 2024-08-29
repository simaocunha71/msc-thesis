
def first_repeated_char(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_repeated_char("abcabc"))

#Exercise3
