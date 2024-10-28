    result = [numbers[0]]
    max_element = numbers[0]

    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        result.append(max_element)

    return result


