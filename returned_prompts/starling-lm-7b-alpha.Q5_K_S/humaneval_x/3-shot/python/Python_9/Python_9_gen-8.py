    result = [numbers[0]]
    max_element = numbers[0]
    for elem in numbers[1:]:
        if elem > max_element:
            result.append(elem)
            max_element = elem
        else:
            result.append(max_element)

    return result


