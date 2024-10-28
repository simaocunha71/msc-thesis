def min_val(lst):
    return min(i for i in lst if type(i) in [int, float])  # Using generator expression and isinstance() function
    # return min(i for i in lst if isinstance(i, (int, float)))  # Using isinstance() function
    # return min(i for i in lst if type(i) in [int, float, complex])  # Using type() function