def text_lowercase_underscore(s: str) -> bool:
    return all(c.islower() or c=='_' for c in s)