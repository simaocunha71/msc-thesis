def start_withp(words):
    pair = ()
    for word in words:
        w = word.split(' ')
        for i in w:
            if i[0].lower() == 'p':
                pair += (i,)
    return pair[:2]