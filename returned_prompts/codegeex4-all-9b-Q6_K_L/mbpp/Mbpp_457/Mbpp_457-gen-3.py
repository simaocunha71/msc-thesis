def Find_Min(lists: list) -> list:
    min_length = min(len(lst) for lst in lists)
    for lst in lists:
        if len(lst) == min_length:
            return lst

