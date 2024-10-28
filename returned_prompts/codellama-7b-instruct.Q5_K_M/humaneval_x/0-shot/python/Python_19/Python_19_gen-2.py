    numbers = numbers.split(" ")
    numbers.sort(key=lambda x: int(x[0]))
    return " ".join(numbers)



