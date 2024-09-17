def find_first_occurrence(sorted_list: list, target: int) -> int:
    first_index = -1
    for i, num in enumerate(sorted_list):
        if num == target:
            if first_index == -1:
                first_index = i
            else:
                return first_index
    return first_index