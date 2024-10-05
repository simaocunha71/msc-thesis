    count = 0

    for idx in range(len(string)):
        if string[idx:].startswith(substring):
            count += 1

    return count


