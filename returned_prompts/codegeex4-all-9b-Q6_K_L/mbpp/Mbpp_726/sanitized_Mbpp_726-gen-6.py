def multiply_elements(numbers):
    result = []
    for i in range(len(numbers)-1):
        result.append(numbers[i] * numbers[i+1])
    return tuple(result)