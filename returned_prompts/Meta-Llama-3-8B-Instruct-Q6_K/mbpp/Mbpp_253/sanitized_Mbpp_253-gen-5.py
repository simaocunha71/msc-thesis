def count_integer(lst):
    return sum(isinstance(x, int) for x in lst)  # Count the number of integers in the list