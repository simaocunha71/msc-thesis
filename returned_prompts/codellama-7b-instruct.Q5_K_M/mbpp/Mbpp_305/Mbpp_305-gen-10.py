
def start_withp(words):
    for w in words:
        if w.split()[0] == 'Python':
            return w.split()
    return None


