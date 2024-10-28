def long_words(n,sentence):
    words=sentence.split()
    long_words=[]
    for i in words:
        if len(i)>n:
            long_words.append(i)
    return long_words