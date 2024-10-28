    boredoms = 0
    for s in S.split('.'):
        if s.startswith('I'):
            boredoms += 1
    return boredoms


