def start_withp(lst):
    for sentence in lst:
        words = sentence.split()
        for word in words:
            if word.lower().startswith('p'):
                return word,