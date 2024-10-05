from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i for n in numbers for i in (n, delimeter)][:-1]


print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]


In this solution, we used list comprehension to create a new list that alternates between each element of the input list and the delimiter. We then return the list excluding the last element, which is the last delimiter.

The time complexity of this solution is O(n), where n is the length of the input list, because we iterate over each element in the input list once. The space complexity is also O(n), because we create a new list of length at most 2n.
"""


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i for n in numbers for i in (n, delimeter)][:-1]


print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]

#tests/test_intersperse.py
from typing import List
import pytest
from intersperse import intersperse


@pytest.mark.parametrize(
    "numbers, delimeter, expected",
    [
        ([], 4, []),
        ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
        ([5, 6, 7, 8], 0, [5, 0, 6, 0, 7, 0, 8]),
        ([-1, -2, -3], -4, [-1, -4, -2, -4, -3]),
    ],
)
def test_intersperse(numbers: List[int],