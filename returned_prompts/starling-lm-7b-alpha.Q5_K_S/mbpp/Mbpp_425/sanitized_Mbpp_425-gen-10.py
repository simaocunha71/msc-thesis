def count_element_in_list(arr, elem):
    c = 0
    for sublist in arr:
        if elem in sublist:
            c += 1
    return c