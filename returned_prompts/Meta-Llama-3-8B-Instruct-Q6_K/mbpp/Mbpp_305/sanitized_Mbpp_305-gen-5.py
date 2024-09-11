def start_withp(lst):
    words = [word for word in lst if word.startswith('p')]
    return tuple(words[:2])