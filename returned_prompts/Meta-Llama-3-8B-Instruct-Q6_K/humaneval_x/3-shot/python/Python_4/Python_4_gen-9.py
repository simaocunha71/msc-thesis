    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)  # type: ignore
    # type: ignore because the variable 'numbers' is not used in the function 'mean_absolute_deviation'  # noqa: E501


