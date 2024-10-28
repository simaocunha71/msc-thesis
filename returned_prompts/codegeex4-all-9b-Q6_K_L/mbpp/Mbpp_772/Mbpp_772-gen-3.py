def remove_length(s: str, k: int) -> str:
    words = s.split(' ')
    new_words = [word for word in words if len(word) != k]
    return ' '.join(new_words)

