def count_Occurrence(tup,list):
    count=0
    for i in list:
        for j in tup:
            if i==j:
                count+=1
    return count