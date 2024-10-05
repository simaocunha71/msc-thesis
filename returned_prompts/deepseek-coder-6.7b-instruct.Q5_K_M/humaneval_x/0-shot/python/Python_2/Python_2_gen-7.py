
    return number % 1


def main():
    print(truncate_number(3.5))


if __name__ == "__main__":
    main()


Output:
0.5


Explanation:
The function truncate_number works by using the modulo operator (%). The modulo operator returns the remainder of the division of the first argument by the second. In the case of truncate_number, it returns the remainder of the division of the number by 1. Since any number divided by 1 remains the same, the remainder of any number divided by 1 is 0. Therefore, this function returns the decimal part of the number.
"""


def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part  (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return number % 1


def main():
    print(truncate_number(3.5))


if __name__ == "__main__":
    main()


Output:
0.5
"""


def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part  (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return number % 1


def main():
    print(truncate_number(3.5))


if __name__ == "__main__":
    main()


Output:
0.5
"""


def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part  (largest integer smaller than given number) and decimals