def recursive_list_sum(lst):
    flat = []
    def flatten(lst):
        for i in lst:
            if isinstance(i, list):
                flatten(i)
            else:
                flat.append(i)
    flatten(lst)
    return sum(flat)