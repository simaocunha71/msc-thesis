    numbers = [x - min(numbers) for x in numbers]
    return [x / max(numbers) for x in numbers]


