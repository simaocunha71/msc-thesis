def larg_nnum(lst, n):
    return heapq.nlargest(n, lst)  # use the heapq module to find the n largest items