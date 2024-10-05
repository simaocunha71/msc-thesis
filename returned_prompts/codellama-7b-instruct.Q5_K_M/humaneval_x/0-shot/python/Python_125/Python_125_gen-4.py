
    return [word for word in txt.split() if word] or txt.translate({ord(c): None for c in " ,."}).count(chr(i)) if i % 2 == 1 for i in range(97, 123)}

