
def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]

def maximum(arr, k):
    return heapq.nlargest(k, arr)

def maximum(arr, k):
    return sorted(arr, key=lambda x: -x)[:k]

def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]

def maximum(arr, k):
    return sorted(arr, key=lambda x: -x)[:k]

def maximum(arr, k):
    return heapq.nlargest(k, arr, key=lambda x: -x)

def maximum(arr, k):
    return sorted(arr, key=lambda x: x, reverse=True)[:k]

def maximum(arr, k):
    return sorted(arr, key=lambda x: -x)[:k]

def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]

def maximum(arr, k):
    return sorted(arr, key=lambda x: -x)[:k]

def maximum(arr, k):
    return heapq.nlargest(k, arr, key=lambda x: -x)
