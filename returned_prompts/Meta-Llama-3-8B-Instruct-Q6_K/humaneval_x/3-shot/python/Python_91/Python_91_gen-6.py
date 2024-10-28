    bored_count = 0
    sentences = S.replace('. ', '.').replace('? ', '?').replace('! ', '!').split('. ')
    for sentence in sentences:
        if sentence and sentence[0].lower() == 'i':
            bored_count += 1
    return bored_count


