    sentences = S.split('. ')
    count = 0
    for sentence in sentences:
        if sentence and sentence[0].lower() == 'i':
            count += 1
    return count


