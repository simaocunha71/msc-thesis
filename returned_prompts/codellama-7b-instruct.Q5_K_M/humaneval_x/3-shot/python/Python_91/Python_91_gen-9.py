    count = 0
    for sentence in S.split('.'):
        for word in sentence.split():
            if word == 'I':
                count += 1
                break
    return count


