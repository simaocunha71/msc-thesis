def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [numbers[i] for i in range(len(numbers))] + [delimeter for i in range(len(numbers) - 1)]
