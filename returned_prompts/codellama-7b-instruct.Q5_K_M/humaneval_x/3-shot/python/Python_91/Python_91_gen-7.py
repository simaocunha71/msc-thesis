    count = 0
    for sentence in S.split(('.', '?', '!')):
        if sentence.startswith('I'):
            count += 1

    return count


