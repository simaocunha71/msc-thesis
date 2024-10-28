
def start_withp(words):
    for word in words:
        if word.startswith('p'):
            return (word.split()[0], word.split()[1])


