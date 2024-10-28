    # Keep track of unique elements.
    unique = set()

    # Iterate over the input list.
    result = []
    for elem in numbers:
        # If the element is unique, append it to the result.
        if elem not in unique:
            unique.add(elem)
            result.append(elem)
    return result



def remove_duplicates_in_place(numbers: List[int]) -> None:
    """ Remove all elements that occur more than once from a list of integers in-place.
    Keep order of elements the same as in the input.
    >>> remove_duplicates_in_place([1, 2, 3, 2, 4])
    >>> numbers
    [1, 3, 4]
    """

    # Keep track of unique elements.
    unique = set()

    # Iterate over the input list.
    for i, elem in enumerate(numbers):
        # If the element is unique, continue to the next element.
        if elem not in unique:
            unique.add(elem)
        else:
            # If the element is a duplicate, remove it from the list.
            del numbers[i]


def remove_duplicates_from_generator(generator: 'Generator[int]') -> 'Generator[int]':
    """ Return a new iterator that generates elements from the input iterator, removing all duplicates.
    >>> for elem in remove_duplicates_from_generator(range(5)):
    ...     print(elem)
    0
    1
    2
    3
    4
    """

    # Keep track of unique elements.
    unique = set()

    # Iterate over the input iterator.
    for elem in generator:
        # If the element is unique, yield it.
        if elem not in unique:
            unique.add(elem)
            yield elem


if __name__ == "__main__":
    import doctest
    doctest.testmod()








































