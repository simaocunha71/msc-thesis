
def sort_array(array):
    if not array:
        return []

    sum_val = sum(array)
    if sum_val % 2 == 0:
        return sorted(array, reverse=True)

    return sorted(array)


B:

def sort_array(array):
    if not array:
        return []

    sum_val = sum(array)
    if sum_val % 2 == 0:
        return sorted(array)

    return sorted(array, reverse=True)