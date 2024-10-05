from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [i / max_val for i in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(i - min_val) / (max_val - min_val) for i in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(i - min_val) / (max_val - min_val) for i in numbers]
# or
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val =