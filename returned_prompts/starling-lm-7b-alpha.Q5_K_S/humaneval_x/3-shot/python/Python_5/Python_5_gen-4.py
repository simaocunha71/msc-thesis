    result = [numbers[0]]
    for i in range(len(numbers)-1):
        result.append(delimeter)
        result.append(numbers[i+1])
    result.append(numbers[-1])
    return result


