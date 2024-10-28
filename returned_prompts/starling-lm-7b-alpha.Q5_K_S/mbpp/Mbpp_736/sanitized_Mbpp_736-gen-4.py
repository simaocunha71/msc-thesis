def left_insertion(list, item):
    i = 0
    while i < len(list) and item > list[i]:
        i += 1
    return i