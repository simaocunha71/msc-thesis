def count_integer(lst):
    return sum(isinstance(x, int) for x in lst)  # This will count the number of integers in the list. 