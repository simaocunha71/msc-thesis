def get_ludic(n):
    primes = [2, 3, 5, 7]
    ludics = []

    for num in range(1, n+1):
        if num in primes:
            ludics.append(num)

    return ludics

print(get_ludic(10))

"""
