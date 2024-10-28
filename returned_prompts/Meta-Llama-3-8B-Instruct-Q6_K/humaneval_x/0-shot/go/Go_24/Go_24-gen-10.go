    if n == 0:
        return 0
    else:
        for i in range(n, 0, -1):
            if n % i == 0:
                return i
    return 1
}

