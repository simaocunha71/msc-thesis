    numbers = [n for n in arr if 1 <= n <= 9]
    numbers.sort()
    numbers.reverse()

    return [str(n) for n in numbers]

