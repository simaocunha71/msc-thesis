def unique_product(lst):
    return reduce(lambda x,y: x*y, set(lst))