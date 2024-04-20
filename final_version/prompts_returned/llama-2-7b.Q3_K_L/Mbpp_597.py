"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    n1 = len(arr1), len(arr2)
    return (find_kth_ii(n1, arr1, k), find_kth_ii(n1, arr2, k)) if n1 == 2 else None

def find_kth_ii(n, a, k):
    """Find index of the element from each array."""
    i = (a[0] - a[1]) // k + 1
    j = n[0] - k - 1
    if i >= j:
        return -1
    while i <= j:
        mid = (i + j) // 2 + 1
        lt_mid = a[mid].lt(a[j])
        rt_mid = a[mid].gt(a[i])
        
        # If the element is present in left side, then return it.
        if rt_mid:
            if lt_mid:
                break
            
            return mid - 1
    
    return i - 1
