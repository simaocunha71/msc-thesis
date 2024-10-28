    boredoms = 0
    for char in S:
        if char == '.' or char == '?' or char == '!':
            if S[0] == 'I':
                boredoms += 1
    return boredoms


