def last(lst, element):
    if element in lst:
        return lst.index(element)
    else:
        return -1

print(last([1,2,3],1))

#assert last([1,2,3],1) == 0
#assert last([1,2,3],2) == 1
#assert last([1,2,3],3) == 2
#assert last([1,2,3],4) == -1

#Solution:
def last(lst, element):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == element:
            return i
    return -1

print(last([1,2,3],1))

#assert last([1,2,3],1) == 0
#assert last([1,2,3],2) == 1
#assert last([1,2,3],3) == 2
#assert last([1,2,3],4) == -1


#Solution:
def last(lst, element):
    try:
        return len(lst) - 1 - lst[::-1].index(element)
    except ValueError:
        return -1

print(last([1,2,3],1))

#assert last([1,2,3],1) == 0
#assert last([1,2,3],2) == 1
#assert last([1,2,3],3) == 2
#assert last([1,2,3],4) == -1

#Solution:
def last(lst, element):
    if element in lst:
        return len(lst) - 1 - lst[::-1].index(element)
    else:
        return -1

print(last([1,2,3],1))

#assert last([1,2,3],1) == 0
#assert last([1,2,3],2) == 1
#assert last([1,2,3],3) == 2
#assert last([1,2,3],4) == -1
<jupyter_output>