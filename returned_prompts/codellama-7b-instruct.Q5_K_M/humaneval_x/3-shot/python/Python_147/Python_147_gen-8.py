    result = 0
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] % 3 == 0:
                    result += 1

    return result


