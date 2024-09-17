def min_product_tuple(lst):
    min_p = (lst[0][0]*lst[0][1], lst[0][0], lst[0][1])
    for i in range(1, len(lst)):
        if min_p[0] > (lst[i][0]*lst[i][1]):
            min_p = (lst[i][0]*lst[i][1], lst[i][0], lst[i][1])
    return min_p