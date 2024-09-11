def count(lst):
    return sum(1 for item in lst if item)  # count the number of True values in the list