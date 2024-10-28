def long_words(n,sentence):
    long_word=[]
    for i in sentence:
        if len(i)>n:
            long_word.append(i)
    return long_word