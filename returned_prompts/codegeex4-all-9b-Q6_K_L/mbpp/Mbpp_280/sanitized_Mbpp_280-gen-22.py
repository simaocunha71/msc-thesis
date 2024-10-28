def sequential_search(arr, element):
    try:
        index = arr.index(element)
        return True, index
    except ValueError:
        return False, -1