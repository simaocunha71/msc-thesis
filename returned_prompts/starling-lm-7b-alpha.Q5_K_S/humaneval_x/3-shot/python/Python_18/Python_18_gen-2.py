    result = 0
    for idx in range(len(string)):
        if string[idx:idx+len(substring)] == substring:
            result += 1

    return result


