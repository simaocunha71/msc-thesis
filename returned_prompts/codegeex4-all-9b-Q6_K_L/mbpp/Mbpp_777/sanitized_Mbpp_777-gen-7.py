def find_sum(lst):
    non_repeated_elements = []
    for num in lst:
        if lst.count(num) == 1:
            non_repeated_elements.append(num)
    return sum(non_repeated_elements)