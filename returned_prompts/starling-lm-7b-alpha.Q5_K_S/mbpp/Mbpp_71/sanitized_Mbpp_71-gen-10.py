def comb_sort(elements):
    """Sort a list of elements using the comb sort algorithm."""
    swapped = True
    gap = len(elements)
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(elements) - gap):
            if elements[i] > elements[i + gap]:
                elements[i], elements[i + gap] = elements[i + gap], elements[i]
                swapped = True
    return elements