    result = 0
    num_of_elements = 0

    for i in range(k):
        result += arr[i]
        num_of_elements += 1

        if num_of_elements == 2:
            break

    return result
