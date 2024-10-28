

def get_positive(l: list):
    return [num for num in l if num > 0]


if __name__ == "____main__":
    import doctest
    doctest.testmod()


def get_positive(l: list):
    return [num for num in l if num > 0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5: Write a Python function to get the sum of the digits of a given number.
<jupyter_code>
def sum_of_digits(n: int):
    """Return the sum of the digits of the given number.
    >>> sum_of_digits(1234)
    10
    >>> sum_of_digits(4321)
    10
    """
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
<jupyter_output>
<empty_output>
<jupyter_text>
Question 6: Write a Python function to check if a given number is a perfect number or not.
<jupyter_code>
def is_perfect(n: int):
    """Return True if the given number is a perfect number, False otherwise.
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(5)
    False
    """
    return sum(i for i in range(1, n) if n % i == 0) == n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
<jupyter_output>
<empty_output>
<jupyter_text>
Question 7: Write a Python function to generate the Fibonacci series up to n terms.
<jupyter_code>
def fibonac