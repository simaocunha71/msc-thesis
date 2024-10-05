    count = 0
    for i in range(n):
        if (i + 1) % 11 == 0 or (i + 1) % 13 == 0:
            count += 1
            number = str(i + 1)
            for j in range(len(number)):
                if number[j] == '7':
                    count += 1
    return count


