
def add_pairwise(my_tuple):
    return tuple(a + b for a, b in zip(my_tuple, my_tuple[1:]))

# or

def add_pairwise(my_tuple):
    result = []
    for i in range(len(my_tuple) - 1):
        result.append(my_tuple[i] + my_tuple[i + 1])
    return tuple(result)


