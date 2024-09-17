def start_withp(words: list) -> tuple:
    p_words = [word for word in words if word.startswith('p')]
    return tuple(p_words[:2])


