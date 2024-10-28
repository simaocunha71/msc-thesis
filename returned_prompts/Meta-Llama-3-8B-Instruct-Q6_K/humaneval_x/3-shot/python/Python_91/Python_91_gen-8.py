    sentences = S.split('. ') + [S.split('. ')[-1]]
    sentences = [s for s in sentences if s]
    return sum(1 for s in sentences if s.strip().lower().startswith('i'))


