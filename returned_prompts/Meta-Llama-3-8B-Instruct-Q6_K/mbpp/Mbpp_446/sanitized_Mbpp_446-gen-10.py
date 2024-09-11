def count_Occurrence(tup, lis):
    return sum(tup.count(i) for i in lis) if isinstance(tup, tuple) else "Input should be a tuple"  # Check if input is tuple, else return error message