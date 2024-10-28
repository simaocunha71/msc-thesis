def max_product_tuple(lst):
    lst.sort()
    return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1], lst[-1][0]*lst[-2][1], lst[-2][0]*lst[-1][1])