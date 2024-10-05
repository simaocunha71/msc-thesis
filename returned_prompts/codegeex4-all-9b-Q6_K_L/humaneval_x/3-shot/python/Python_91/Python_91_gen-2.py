    count = 0
    sentences = S.split('. ')
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count


