def consecutive_duplicates(numbers):
    """Remove consecutive duplicates of a given list"""
    result = []
    for i in range(len(numbers)):
        if i == 0 or numbers[i] != numbers[i-1]:
            result.append(numbers[i])
    return result