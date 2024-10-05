    def pluck(arr):
        # Initialize result
        result = [float('inf'), float('inf')]

        # Find the smallest even value and its index
        for idx, elem in enumerate(arr):
            if elem % 2 == 0 and elem < result[0]:
                result[0] = elem
                result[1] = idx

        # Return result if found, else []
        return result if result[0] != float('inf') else []


def pluck(arr):
    result = [float('inf'), float('inf')]
    for idx, elem in enumerate(arr):
        if elem % 2 == 0 and elem < result[0]:
            result[0] = elem
            result[1] = idx
    return result if result[0] != float('inf') else []


