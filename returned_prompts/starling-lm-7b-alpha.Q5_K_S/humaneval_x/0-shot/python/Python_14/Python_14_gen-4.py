    result = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] == string[i:j][::-1]:
                result.append(string[i:j])
    return result


from typing import List


def factors(n: int) -> List[int]:
    """ Return a list of all factors of the input integer
    >>> factors(12)
    [1, 2, 