    result = 0
    idx = 0
    while idx < len(S):
        if S[idx] == 'I':
            result += 1
            while S[idx] != '.' and S[idx] != '?' and S[idx] != '!':
                idx += 1
        idx += 1
    return result


