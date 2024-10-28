    result = []
    max_element = numbers[0]

    for number in numbers:
        if number > max_element:
            max_element = number
        result.append(max_element)

    return result


