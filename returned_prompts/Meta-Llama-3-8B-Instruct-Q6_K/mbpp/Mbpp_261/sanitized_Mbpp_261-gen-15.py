def division_elements(tuple1, tuple2):
    result = []
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    for num1, num2 in zip(tuple1, tuple2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result.append(num1 / num2)
    return tuple(result)