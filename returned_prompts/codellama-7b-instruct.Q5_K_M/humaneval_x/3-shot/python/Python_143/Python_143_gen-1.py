    words = sentence.split()
    return ' '.join(word for word in words if len(word) % 2 == 1)


