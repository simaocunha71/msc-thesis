from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    return sum(numbers), eval('*'.join(map(str, numbers)))
    # return sum(numbers), functools.reduce(lambda x, y: x * y, numbers)
    # return sum(numbers), math.prod(numbers)
    # return sum(numbers), 1
    # return sum(numbers), reduce(lambda x, y: x * y, numbers, 1)
    # return sum(numbers), 1 if numbers else 0
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 0
    # return sum(numbers), 1 if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0] if numbers else 1
    # return sum(numbers), numbers[0