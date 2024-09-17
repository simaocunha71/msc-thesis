def count_Occurrence(tup,lis):
    count = 0
    for i in lis:
        for j in tup:
            if i==j:
                count+=1
    return count