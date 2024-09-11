def max_xor(arr):
    max_so_far = 0
    max_here = 0
    for n in arr:
        max_here = max(max_here, n)
        max_so_far = max(