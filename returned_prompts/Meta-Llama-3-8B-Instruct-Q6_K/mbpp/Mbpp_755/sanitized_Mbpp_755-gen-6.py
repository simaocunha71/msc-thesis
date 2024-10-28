def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    sorted_lst = sorted(lst)
    return sorted_lst[1] if sorted_lst[1] != sorted_lst[0] else min([x for x in sorted_lst if x != sorted_lst[0]]) if len(set(sorted_lst)) > 1 else None