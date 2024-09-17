def find_dissimilar(t1, t2):
    dissimilar_elements = []
    for element in t1:
        if element not in t2:
            dissimilar_elements.append(element)
    for element in t2:
        if element not in t1:
            dissimilar_elements.append(element)
    return tuple(sorted(dissimilar_elements))