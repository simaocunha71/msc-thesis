def start_withp(words):
    p_words = [word for word in words if word.lower().startswith('p')]
    if len(p_words) >= 2:
        return tuple(p_words[:2])
    else:
        return tuple(p_words)