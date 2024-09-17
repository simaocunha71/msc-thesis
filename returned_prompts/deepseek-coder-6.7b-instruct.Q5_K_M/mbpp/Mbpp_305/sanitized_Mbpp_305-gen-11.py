def start_withp(lst):
    for i in lst:
        words = i.split()
        for word in words:
            if word.lower().startswith('p'):
                return word,