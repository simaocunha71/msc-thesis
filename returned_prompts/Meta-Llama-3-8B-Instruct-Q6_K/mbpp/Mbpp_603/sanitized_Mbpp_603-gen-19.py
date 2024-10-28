def get_ludic(n):
    lucid_numbers = []
    for i in range(1, n+1):
        if all(i % j for j in range(2, int(i**0.5) + 1)):
            lucid_numbers.append(i)
    return lucid_numbers