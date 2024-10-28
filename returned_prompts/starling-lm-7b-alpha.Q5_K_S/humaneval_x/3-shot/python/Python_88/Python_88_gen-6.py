    # Initialize result array with the same length as the input array
    result = [x for x in array]

    # Sort the array in ascending order if the sum of the first and last element is odd, otherwise sort in descending order
    if (result[0] + result[-1]) % 2 == 0:
        result.sort(reverse=True)
    else:
        result.sort()

    return result


