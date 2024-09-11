def count_Occurrence(tuple_list: tuple, element_list: list) -> int:
    count = 0
    for element in element_list:
        count += tuple_list.count(element)
    return count