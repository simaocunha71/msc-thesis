def start_withp(lst):
    for words in lst:
        for word in words.split():
            if word.lower().startswith('p'):
                return word,