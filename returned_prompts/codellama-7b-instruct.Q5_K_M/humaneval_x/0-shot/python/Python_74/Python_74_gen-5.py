
def total_match(lst1, lst2):
    count1=0
    count2=0
    for i in lst1:
        count1+=len(i)
    for j in lst2:
        count2+=len(j)
    if count1>count2:
        return lst1
    else:
        return lst2