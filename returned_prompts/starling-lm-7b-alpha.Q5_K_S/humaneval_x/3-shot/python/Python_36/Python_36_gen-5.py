    count = 0
    for i in range(n - 11, n + 1, 11):
        if i % 13 == 0:
            if str(i).count('7') > 0:
                count += 1
    return count


