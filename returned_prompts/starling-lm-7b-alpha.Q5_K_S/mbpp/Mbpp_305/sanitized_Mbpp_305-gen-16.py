def start_withp(words: list) -> str:
    p_words = [word for word in words if word.startswith('p')]
    if len(p_words) >= 2:
        return p_words[:2]
    else:
        return None