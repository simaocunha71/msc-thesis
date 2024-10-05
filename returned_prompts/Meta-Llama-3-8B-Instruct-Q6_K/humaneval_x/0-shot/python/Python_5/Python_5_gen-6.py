def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [n for i, n in enumerate(numbers + [numbers[-1] + 1]) if i % 2 == 0] + [delimeter] + [n for i, n in enumerate(numbers + [numbers[-1] + 1], 1) if i % 2 != 0]
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        result.append(n)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [n for i, n in enumerate(numbers) if i % 2 == 0] + [delimeter] + [n for i, n in enumerate(numbers, 1) if i % 2 != 0]
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i == 0:
            result.append(n)
        else:
            result.append(delimeter)
            result.append(n)
    return result
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [numbers[0]] + [delimeter] + [n for n in numbers[1:]]
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i == 0:
            result.append(n)
        else:
            result.append(delimeter)
            result.append(n)
    return result
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [n for i, n in enumerate(numbers) if i % 2 == 0] + [delimeter] + [n for i, n in enumerate(numbers, 1) if i % 2 != 0]
# or
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i == 0:
            result.append(n)
        else:
            result.append(delimeter)
            result.append(n)
    return result