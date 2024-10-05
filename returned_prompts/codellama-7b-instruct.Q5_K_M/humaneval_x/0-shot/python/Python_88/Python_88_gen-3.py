
def sort_array(array):
    array = sorted(array)
    if sum(array[:2]) % 2 == 0:
        array.reverse()
    return array
