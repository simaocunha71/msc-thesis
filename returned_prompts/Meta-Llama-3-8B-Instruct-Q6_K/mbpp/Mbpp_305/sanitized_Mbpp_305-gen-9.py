def start_withp(words):
    result = [word for word in words if word.startswith('p')]
    return tuple(result[0].split()[0], result[1].split()[0]) if len(result) > 1 else ('', '')