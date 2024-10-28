    result = ""
    for i in range(min(len(a), len(b))):
        result += str(int(a[i]) ^ int(b[i]))
    return result


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['011', '001'])
    ['101', '111']
    """
    if len(a) != len(b):
        raise ValueError('The given lists of strings must be of equal length')
    result = []
    for i in range(len(a)):
        result.append(string_xor(a[i], b[i]))
    return result


def string_xor_list_iter(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list_iter(['010', '110'], ['011', '001'])
    ['101', '111']
    """
    if len(a) != len(b):
        raise ValueError('The given lists of strings must be of equal length')
    result = []
    for i in range(len(a)):
        result.append(string_xor(a[i], b[i]))
    return result


def string_xor_iter(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_iter('010', '110')
    '100'
    """
    result = ''
    for i