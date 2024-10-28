    count = 0
    for sentence in S.split('. ') + [S]:
        if sentence and sentence[0].lower() == 'i':
            count += 1
    return count


