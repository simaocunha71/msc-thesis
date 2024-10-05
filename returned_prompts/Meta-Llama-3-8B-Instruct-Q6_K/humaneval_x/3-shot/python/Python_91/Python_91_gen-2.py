    boredom_count = 0
    sentences = S.split('. ')
    for sentence in sentences:
        if sentence and sentence[0].lower() == 'i':
            boredom_count += 1
    return boredom_count


