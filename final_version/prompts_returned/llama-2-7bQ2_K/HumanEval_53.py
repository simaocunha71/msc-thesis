

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


def sub(x: int, y: int):
    """Subtraction of two numbers x and y
    >>> sub(4, -2)
    2
    >>> sub(0, 3)
    -1
    """
    return x - y


def mul(x: int, y: int):
    """Multiply a number x by y
    >>> mul(5, 2)
    10
    >>> mul(-3, -2)
    -6
    """
    return x * y


def div(dividend: float, divisor: float):
    """Divide two numbers with each other. Return the result in float
    >>> div(5, 2)
    2.0
    >>> div(-3, -2)
    -1.5
    """
    return dividend / divisor
