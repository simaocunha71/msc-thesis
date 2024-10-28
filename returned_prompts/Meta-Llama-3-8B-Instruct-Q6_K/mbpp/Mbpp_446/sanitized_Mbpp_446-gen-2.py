def count_Occurrence(tup, elements):
    count = 0
    for element in elements:
        count += tup.count(element)
    return count