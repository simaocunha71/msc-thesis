import heapq
def larg_nnum(lst: list,n: int) -> list:
    return heapq.nlargest(n, lst)