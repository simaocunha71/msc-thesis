
def remove_length(s: str, k: int) -> str:
    words = s.split()
    return ' '.join(word for word in words if len(word) != k)


