    sentences = S.split('. ')
    boredoms = [sentence for sentence in sentences if sentence and sentence.split()[0].lower() == 'i']
    return len(boredoms) if isinstance(S, str) else None


