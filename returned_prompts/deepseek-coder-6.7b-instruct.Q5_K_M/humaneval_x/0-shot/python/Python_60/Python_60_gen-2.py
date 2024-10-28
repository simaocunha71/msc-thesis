

def sum_to_n(n: int):
    return sum(range(1, n + 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# or

def sum_to_n(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    print(sum_to_n(30))
    print(sum_to_n(100))
    print(sum_to_n(5))
    print(sum_to_n(10))
    print(sum_to_n(1))


# or

def sum_to_n(n: int):
    return sum(i for i in range(1, n + 1))


if __name__ == "__main__":
    print(sum_to_n(30))
    print(sum_to_n(100))
    print(sum_to_n(5))
    print(sum_to_n(10))
    print(sum_to_n(1))

# or

def sum_to_n(n: int):
    return sum({i: i for i in range(1, n + 1)}.values())


if __name__ == "__main__":
    print(sum_to_n(30))
    print(sum_to_n(100))
    print(sum_to_n(5))
    print(sum_to_n(10))
    print(sum_to_n(1))


# or

def sum_to_n(n: int):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)


if __name__ == "__main__":
    print(sum_to_n(30))
    print(sum_to_n(100))
    print(sum_to_n(5))
    print(sum_to_n(10))