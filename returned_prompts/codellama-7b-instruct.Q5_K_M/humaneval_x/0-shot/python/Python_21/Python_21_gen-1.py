def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [i - min(numbers) for i in numbers] / max(numbers) - min(numbers)

