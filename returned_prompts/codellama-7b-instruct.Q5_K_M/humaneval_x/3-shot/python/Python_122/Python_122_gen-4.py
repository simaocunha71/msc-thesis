    result = 0

    for i in range(k):
        result += arr[i]
        if len(str(result)) > 2:
            break

    return result


