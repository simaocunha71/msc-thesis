def issort_list(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True

print(issort_list([1,2,4,6,8,10,12,14,16,17]))

#