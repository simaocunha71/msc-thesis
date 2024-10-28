def extract_nth_element(lst, n):
    if n >= len(lst):
        return []
    return [i[0] for i in lst[:n+1]]