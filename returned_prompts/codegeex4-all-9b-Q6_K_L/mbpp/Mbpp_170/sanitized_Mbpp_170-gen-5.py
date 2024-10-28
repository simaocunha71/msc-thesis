def sum_range_list(lst, start, end):
    if start < 0 or end >= len(lst) or start > end:
        raise ValueError("Invalid range")
    return sum(lst[start:end+1])