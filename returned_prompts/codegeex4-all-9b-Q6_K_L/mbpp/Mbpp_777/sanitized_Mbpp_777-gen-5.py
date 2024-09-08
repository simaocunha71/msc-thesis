def find_sum(lst):
    unique_elements = []
    for element in lst:
        if lst.count(element) == 1:
            unique_elements.append(element)
    return sum(unique_elements)