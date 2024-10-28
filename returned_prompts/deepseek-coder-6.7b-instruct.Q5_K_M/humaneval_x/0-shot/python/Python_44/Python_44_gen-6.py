
    if x == 0:
        return "0"
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return "".join(digits[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()


```

## Python 101 - Check if a string is a palindrome

