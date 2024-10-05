

def modp(n: int, p: int):
    return pow(2, n, p)


def main():
    tests = [
        (3, 5, 3),
        (1101, 101, 2),
        (0, 101, 1),
        (3, 11, 8),
        (100, 101, 1),
    ]
    for t in tests:
        assert modp(*t) == modp(*t)


if __name__ == "__main__":
    main()