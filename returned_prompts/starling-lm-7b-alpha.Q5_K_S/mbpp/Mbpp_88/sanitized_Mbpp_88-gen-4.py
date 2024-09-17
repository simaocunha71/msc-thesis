def freq_count(lst):
    dct={}
    for i in lst:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct