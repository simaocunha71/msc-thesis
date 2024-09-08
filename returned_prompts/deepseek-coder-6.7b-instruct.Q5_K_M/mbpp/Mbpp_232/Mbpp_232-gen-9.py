def larg_nnum(lst,n):
    lst.sort(reverse=True)
    return lst[:n]
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))

#or

def larg_nnum(lst,n):
    return sorted(lst, reverse=True)[:n]
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))

#or

import heapq
def larg_nnum(lst,n):
    return heapq.nlargest(n,lst)
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))

#or

def larg_nnum(lst,n):
    return sorted(lst)[-n:]
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))

#or

import operator
def larg_nnum(lst,n):
    return list(reversed(sorted(lst)[-n:]))
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))

#or

def larg_nnum(lst,n):
    return sorted(lst)[::-1][:n]
print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 