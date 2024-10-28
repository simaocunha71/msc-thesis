    boredoms = 0
    for word in S.split('.'):
        if word.strip().startswith('I'):
            boredoms += 1
    return boredoms


