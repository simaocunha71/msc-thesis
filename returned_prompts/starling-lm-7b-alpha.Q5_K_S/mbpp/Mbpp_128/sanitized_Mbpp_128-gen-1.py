def long_words(n,string):
    return [i for i in string.split() if len(i)>n]