def extract_nth_element(lst, n):
    return [x[0] for x in lst] if n == 0 else [x[1] for x in lst] if n == 1 else [x[2] for x in lst] if n == 2 else None