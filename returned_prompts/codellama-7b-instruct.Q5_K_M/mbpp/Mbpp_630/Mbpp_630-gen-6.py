
from typing import List


def get_coordinates(coordinate_tuple: tuple) -> List[list]:
    """
    >>> get_coordinates((3, 4))
    [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    """
    x, y = coordinate_tuple
    return [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y], [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
