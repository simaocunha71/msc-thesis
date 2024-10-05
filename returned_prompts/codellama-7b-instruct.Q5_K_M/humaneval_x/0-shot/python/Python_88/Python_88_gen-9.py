
def sort_array(array):
    array = sorted(array, key=lambda x: x, reverse=False)
    if sum(array) % 2 == 0:
        array = sorted(array, key=lambda x: x, reverse=True)
    return array

