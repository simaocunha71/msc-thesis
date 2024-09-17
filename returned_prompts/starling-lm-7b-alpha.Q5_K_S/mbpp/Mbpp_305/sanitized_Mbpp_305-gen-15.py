def start_withp(words):
    words = [word for word in words if word.startswith('p')]
    if len(words) == 2:
        return tuple(words)
    else:
        return tuple(words[:2])