"""
def max_product_tuple(lst):
    lst.sort()
    return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1], lst[-1][0]*lst[-2][1], lst[-2][0]*lst[-1][1])

# def max_product_tuple(lst):
#     lst.sort()
#     return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1])

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    lst.sort()
    return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1], lst[-1][0]*lst[-2][1], lst[-2][0]*lst[-1][1])

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36

def max_product_tuple(lst):
    lst.sort()
    if len(lst) == 2:
        return lst[0][0]*lst[0][1]
    elif len(lst) == 3:
        return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1])
    else:
        return max(lst[0][0]*lst[0][1], lst[-1][0]*lst[-1][1], lst[-1][0]*lst[-2][1], lst[-2][0]*lst[-1][1])

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36

def max_product_tuple(lst):
    lst.sort()
    if len(lst) == 2:
        return lst[0][0]*lst[0][1]
    elif len(lst) == 