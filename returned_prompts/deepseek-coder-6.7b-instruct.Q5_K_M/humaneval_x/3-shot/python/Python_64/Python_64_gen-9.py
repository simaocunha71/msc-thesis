    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    if s[-1] == 'y':
        count += 1
    return count


