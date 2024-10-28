    result = 0
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            result += 1

    return result


