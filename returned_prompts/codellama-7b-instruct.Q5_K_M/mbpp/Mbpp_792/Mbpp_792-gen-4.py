def count_list(lst):
    count = 0
    for element in lst:
        if type(element) == list:
            count += 1
            count += count_list(element)
    return count

