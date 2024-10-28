def extract_nth_element(tuples_list, n):
    return [tup for i, tup in enumerate(tuples_list) if i == n] or [None]  # Return None if n is out of range