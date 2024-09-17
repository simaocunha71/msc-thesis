def reverse_words(string):
    l = []
    for word in string.split():
        l.append(word)
    l.reverse()
    return " ".join(l)