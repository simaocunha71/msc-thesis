    mean_val = sum(numbers) / len(numbers)
    abs_diffs = [abs(x - mean_val) for x in numbers]
    return sum(abs_diffs) / len(abs_diffs)


