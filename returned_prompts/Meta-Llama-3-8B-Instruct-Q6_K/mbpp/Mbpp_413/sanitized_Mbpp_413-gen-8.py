def extract_nth_element(lst, n):
    return [tup for i, tup in enumerate(lst) if i == n]