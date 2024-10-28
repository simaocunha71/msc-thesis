import heapq
def expensive_items(dataset,n):
    return heapq.nlargest(n,dataset,key=lambda x:x['price'])
