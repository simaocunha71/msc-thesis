def count_integer(lst):
    return sum(isinstance(x, int) for x in lst)  # Pythonic way
    # or
    # count = 0
    # for x in lst:
    #     if isinstance(x, int):
    #         count += 1
    # return count