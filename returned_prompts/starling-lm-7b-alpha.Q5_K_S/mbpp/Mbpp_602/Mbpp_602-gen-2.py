
def first_repeated_char(s: str) -> str:
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            return s[i]
    return "No repeated character found."


