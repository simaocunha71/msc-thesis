def count_Occurrence(tuple_list, elements):
    count = 0
    for element in elements:
        for item in tuple_list:
            if item == element:
                count += 1
    return count