    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1

    return count


