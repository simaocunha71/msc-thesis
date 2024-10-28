    result = []

    for i, node in enumerate(arr):
        if node % 2 == 0:
            result = [node, i]

    return result if result else []


