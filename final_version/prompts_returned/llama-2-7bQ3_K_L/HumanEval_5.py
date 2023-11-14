from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # If the input list is empty, return an empty list. Else add delimeter between every two consecutive items in the list. Return the list after inserting delimeters.
    if not numbers:
        return []

    for idx, num in enumerate(numbers):
        if (idx + 1) % 2 == 0 and len(numbers) != 1:
            print(f"Adding {num} to the list.")
            return [*list(numbers), delimeter] + [delimeter] * (2 - len(numbers))

    return numbers[:-1] + [delimeter] * (len(numbers)) + numbers[1:]
