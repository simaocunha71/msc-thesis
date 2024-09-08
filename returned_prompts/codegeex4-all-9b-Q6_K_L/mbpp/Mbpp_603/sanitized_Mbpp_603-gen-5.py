def get_ludic(n):
    ludic_numbers = []
    for i in range(1, n+1):
        if all(i % j != 0 for j in range(2, i)):
            ludic_numbers.append(i)
    return ludic_numbers