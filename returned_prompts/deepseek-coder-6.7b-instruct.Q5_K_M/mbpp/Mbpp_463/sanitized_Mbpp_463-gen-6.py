def max_subarray_product(lst):
    max_end_here = max_end_so_far = 1
    for i in lst:
        if i == 0:
            max_end_here = max_end_so_far = 1
        else:
            max_end_here = max(i, max_end_here * i)
            max_end_so_far = max(max_end_so_far, max_end_here)
    return max_end_so_far