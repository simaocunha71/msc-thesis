def list_split(lst,n):
    lst_new = []
    for i in range(0,len(lst),n):
        lst_new.append(lst[i:i+n])
    return lst_new