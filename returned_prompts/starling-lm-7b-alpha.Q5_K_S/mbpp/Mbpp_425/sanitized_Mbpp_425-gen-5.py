def count_element_in_list(matrix, element):
    count = 0
    for sublist in matrix:
        if element in sublist:
            count += 1
    return count