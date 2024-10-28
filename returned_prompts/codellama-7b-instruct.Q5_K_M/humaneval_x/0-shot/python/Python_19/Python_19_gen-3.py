    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x))
    return " ".join(numbers)


