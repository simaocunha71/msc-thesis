
def digitSum(s):
    """
    Parameters
    ----------
    s : str
        The string to be evaluated.

    Returns
    -------
    int
        The sum of the upper characters' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())


def digitSum(s):
    """
    Parameters
    ----------
    s : str
        The string to be evaluated.

    Returns
    -------
    int
        The sum of the upper characters' ASCII codes.
    """
    total = 0
    for c in s:
        if c.isupper():
            total += ord(c)
    return total


def digitSum(s):
    """
    Parameters
    ----------
    s : str
        The string to be evaluated.

    Returns
    -------
    int
        The sum of the upper characters' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())


def digitSum(s):
    """
    Parameters
    ----------
    s : str
        The string to be evaluated.

    Returns
    -------
    int
        The sum of the upper characters' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())


def digitSum(s):
    """
    Parameters
    ----------
    s : str
        The string to be evaluated.

    Returns
    -------
    int
        The sum of the upper characters' ASCII codes.
    """
    total = 0
    for c in s:
        if c.isupper():
            total += ord(c)
    return total

def digitSum(s):
    total = 0
    for c in s:
        if c.isupper():
            total += ord(c)
    return total



# Run tests
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 