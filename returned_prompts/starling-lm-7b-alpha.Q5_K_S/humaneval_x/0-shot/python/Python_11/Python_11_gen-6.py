    res = ''
    for i in range(min(len(a), len(b))):
        res += str(int(a[i]) ^ int(b[i]))
    return res


def list_xor(a: List[int], b: List[int]) -> List[int]:
    """ Input are two lists of ints.
    Perform XOR on these inputs and return result also as a list.
    >>> list_xor([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    """
    if len(a) != len(b):
        raise ValueError('Lengths of lists must be equal!')

    res = []
    for i in range(len(a)):
        res.append(a[i] ^ b[i])

    return res


def string_to_int(a: str) -> int:
    """ Convert input string to an integer.
    >>> string_to_int('10')
    10
    """
    return int(a)


def int_to_string(a: int) -> str:
    """ Convert input integer to a string.
    >>> int_to_string(10)
    '10'
    """
    return str(a)


def list_to_string(a: List[int]) -> str:
    """ Convert input list of integers to a string.
    >>> list_to_string([1, 2, 3])
    '1,2,3'
    """
    return ','.join([int_to_string(num) for num in a])


def string_to_list(a: str) -> List[int]:
    """ Convert input string of integers to a list.
    >>> string_to_list('10,20,30')
    [10, 20, 30]
    """
    return [int(num) for num in a.split(',')]


def list_to_dict(a: List[int], b: List[str]) -> dict:
    """ Convert two lists of equal length to a