
def check_min_heap(lst):
    n = len(lst)
    for i in range(int(n/2)-1):
        if lst[i] > lst[2*i+1]:
            return False
        if 2*i+2 < n:
            if lst[i] > lst[2*i+2]:
                return False
    return True
"""
The function works by checking each parent node, if it is smaller than both of its child nodes then it is a min heap.
"""

