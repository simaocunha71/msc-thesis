def find_sum(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    non_repeated_elements = [element for element, count in counts.items() if count == 1]
    return sum(non_repeated_elements)