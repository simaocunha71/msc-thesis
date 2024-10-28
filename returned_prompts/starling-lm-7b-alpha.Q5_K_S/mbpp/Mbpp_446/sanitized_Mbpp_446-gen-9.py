def count_Occurrence(tup,list):
    cnt=0
    for i in tup:
        if i in list:
            cnt+=list.count(i)
    return cnt