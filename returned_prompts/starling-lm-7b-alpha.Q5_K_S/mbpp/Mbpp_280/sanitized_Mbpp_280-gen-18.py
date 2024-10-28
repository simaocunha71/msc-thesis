def sequential_search(array: list, element: int) -> tuple:
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)