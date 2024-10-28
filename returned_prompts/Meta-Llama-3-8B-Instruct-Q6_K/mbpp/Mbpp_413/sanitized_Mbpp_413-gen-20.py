def extract_nth_element(lst, n):
    if n<0:
        raise ValueError("n should be a non-negative integer")
    if n >= len(lst):
        raise ValueError("n is out of range")
    return [tup for i, tup in enumerate(lst) if i==n]