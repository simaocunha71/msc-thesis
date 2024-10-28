def multiply_elements(numbers_tuple):
    result = ()
    for i in range(len(numbers_tuple) - 1):
        result += (numbers_tuple[i] * numbers_tuple[i + 1],)
    return result