def even_position(lst):
    return all(i%2 == 0 and isinstance(i, int) and i%2 == 0 for i in lst[1::2])  # checking for even numbers at even positions
    # return all(i%2 == 0 for i in lst[1::2])  # checking for even numbers at even positions