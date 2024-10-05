def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """

    result = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

# Tests
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]



