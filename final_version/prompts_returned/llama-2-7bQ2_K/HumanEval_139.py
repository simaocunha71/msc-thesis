
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    def _brazilian_factorial(n):
        return int(f"{1}! * ({(n-1)}!)!"[3:-2]) / n

    return _brazilian_factorial


def main():
    special_factorial = special_factorial(4)  # special_factorial(1),
                                             # special_factorial(2),
                                             # special_factorial(3),
                                             # special_factorial(4),
                                             # etc.
    print("special factorial of 4 is {}\n".format(special_factorial))

if __name__ == "__main__":
    main()