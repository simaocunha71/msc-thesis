def remove_length(string: str, k: int) -> str:
    words = string.split(' ')
    result = [word for word in words if len(word) != k]
    return ' '.join(result)