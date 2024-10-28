    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes
    # return tuple(map(lambda x: len(list(filter(lambda y: str(y) == str(y)[::-1], range(1, n, x))), (2, 1)))
    # return tuple(map(lambda x: sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % x == 0), (2, 1)))
    # return (sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 == 0), sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 != 0))  # or any other one-liner solution
    # return tuple(map(lambda x: sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % x == 0), (2, 1)))  # or any other one-liner solution
    # return (sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 == 0), sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 != 0))  # or any other one-liner solution
    # return tuple(map(lambda x: sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % x == 0), (2, 1)))  # or any other one-liner solution
    # return (sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 == 0), sum(1 for i in range(1, n) if str(i) == str(i)[::-1] and i % 2 != 0))  # or any other one