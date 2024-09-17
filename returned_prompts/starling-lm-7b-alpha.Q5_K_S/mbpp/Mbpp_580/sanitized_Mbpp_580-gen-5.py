from typing import Tuple
def extract_even(input_tuple: Tuple) -> Tuple:
    result = []
    for i in input_tuple:
        if isinstance(i, tuple):
            result.append(extract_even(i))
        elif isinstance(i, int):
            if i % 2 == 0:
                result.append(i)
    return tuple(result)