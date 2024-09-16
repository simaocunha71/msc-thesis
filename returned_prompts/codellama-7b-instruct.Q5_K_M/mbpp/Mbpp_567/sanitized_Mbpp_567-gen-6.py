def issort_list(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            return False
    return True