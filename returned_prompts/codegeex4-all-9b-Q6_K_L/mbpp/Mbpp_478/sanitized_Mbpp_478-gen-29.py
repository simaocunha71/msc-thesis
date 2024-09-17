def remove_lowercase(s: str) -> str:
    for c in s:
        if c.islower():
            s = s.replace(c,"")
    return s