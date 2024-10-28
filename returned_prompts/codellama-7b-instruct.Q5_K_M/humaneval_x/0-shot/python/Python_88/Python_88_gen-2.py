
def sort_array(array):
    if not array:
        return []
    array.sort()
    if sum(array) % 2 == 0:
        return array[::-1]
    return array
