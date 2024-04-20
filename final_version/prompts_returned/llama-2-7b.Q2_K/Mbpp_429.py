"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
from typing import Union

def and_tuples(x: Union[str, [int], [float]]) -> Union[List[Union[int]], List[Tuple[int, ...]]]:
    if isinstance(x, str):
        x = eval(x)
    elif isinstance(x, [int]):
        return [x]  # just pass it through directly.
    else:
        x = list(mapЪ(float, x))  # convert x to a list of floats and then map it into tuple for ease of use.
    return [(a, b) for a, b in izip(x[0], x[1])]
