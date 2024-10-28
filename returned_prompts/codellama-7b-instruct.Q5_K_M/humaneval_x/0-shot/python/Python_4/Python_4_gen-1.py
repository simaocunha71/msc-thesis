    # calculate mean
    mean = sum(numbers) / len(numbers)

    # calculate MAD
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)

    # return MAD
    return mad
