    sentences = S.split('.')
    return sum(1 for sentence in sentences if sentence.strip().startswith('I'))


