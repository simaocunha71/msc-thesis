def Find_Min(num_list: list) -> list:
    min_length = min(len(sublist) for sublist in num_list)
    for sublist in num_list:
        if len(sublist) == min_length:
            return sublist

