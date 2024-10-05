    abs_differences = [abs(number - mean) for number in numbers]
    return sum(abs_differences) / len(numbers)


