import heapq
import operator
def larg_nnum(lst,n):
    lst.sort(reverse=True)
    return lst[:n]