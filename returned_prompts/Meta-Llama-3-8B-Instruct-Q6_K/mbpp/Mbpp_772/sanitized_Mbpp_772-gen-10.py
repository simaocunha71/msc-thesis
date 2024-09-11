def remove_length(s: str, k: int) -> str:
    return ' '.join([word for word in s.split() if len(word) != k])  # use list comprehension to filter out words of length k