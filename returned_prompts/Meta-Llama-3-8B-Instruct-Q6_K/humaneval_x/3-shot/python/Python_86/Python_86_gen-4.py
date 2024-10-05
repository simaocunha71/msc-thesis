    words = s.split()
    result = []

    for word in words:
        new_word = ''.join(sorted(word))
        result.append(new_word)

    return ' '.join(result)  # or ''.join(result) for no spaces between words


