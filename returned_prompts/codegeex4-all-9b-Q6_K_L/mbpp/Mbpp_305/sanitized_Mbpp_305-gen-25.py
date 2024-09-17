def start_withp(words: list) -> tuple:
    for word in words:
        if word.startswith('p'):
            return (word.split()[0], word.split()[1])