def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i, v in enumerate(numbers):
        for w in numbers[i+1:]:
            if abs(v-w) < threshold:
                return True
    return False