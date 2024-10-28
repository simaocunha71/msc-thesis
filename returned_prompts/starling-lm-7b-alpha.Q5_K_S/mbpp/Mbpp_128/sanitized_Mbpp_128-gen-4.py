def long_words(n,sentence):
    words=sentence.split(" ")
    result=[]
    for word in words:
        if len(word)>n:
            result.append(word)
    return result