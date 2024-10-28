def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


if __name__ == "____main__":
    import doctest
    doctest.testmod()

"""
This function is taking a list of integers 'numbers' and an integer 'delimeter' as input. 
It is returning a new list where the 'delimeter' is inserted between every two consecutive elements of the input list.
If the input list is empty, it returns an empty list.
"""

#src/intersperse_solution.py
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

#src/intersperse_solution_test.py
from intersperse_solution import intersperse


def test_intersperse_empty_list():
    assert intersperse([], 4) == []


def test_intersperse_single_element():
    assert intersperse([1], 4) == [1]


def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_delimeter_zero():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]


def test_intersperse_delimeter_negative():
    assert intersperse([1, 2, 3], -1) == [1, -