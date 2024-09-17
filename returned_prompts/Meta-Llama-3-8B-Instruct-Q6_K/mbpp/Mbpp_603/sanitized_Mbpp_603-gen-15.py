def get_ludic(n):
    lucid_numbers = set()
    for i in range(1, n+1):
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            lucid_numbers.add(i)
    return sorted(list(lucid_numbers))