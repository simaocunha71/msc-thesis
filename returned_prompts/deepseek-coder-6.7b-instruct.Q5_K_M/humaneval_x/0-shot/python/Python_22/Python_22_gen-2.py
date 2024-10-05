from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]


print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]


