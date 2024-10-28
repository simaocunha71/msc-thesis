    def to_bin(n: int) -> str:
        """ Convert given number to binary representation.
        >>> to_bin(0)
        '0'
        >>> to_bin(1)
        '1'
        >>> to_bin(2)
        '10'
        """
        return "{0:b}".format(n)

    def to_decimal(bin_str: str) -> int:
        """ Convert given binary representation to decimal number.
        >>> to_decimal('0')
        0
        >>> to_decimal('1')
        1
        >>> to_decimal('10')
        2
        """
        return int(bin_str, 2)

    def to_sum(decimal: int) -> int:
        """ Convert given decimal number to sum of digits in binary representation.
        >>> to_sum(0)
        0
        >>> to_sum(1)
        1
        >>> to_sum(2)
        3
        """
        return bin(decimal).count("1")

    return to_sum(to_decimal(to_bin(N)))




def main():
    print(solve(1000))
    print(solve(150))
    print(solve(147))

if __name__ == "__main__":
    main()


