def remove_length(s: str, k: int) -> str:
    words = s.split()
    words = [word for word in words if len(word) != k]
    return " ".join(words)