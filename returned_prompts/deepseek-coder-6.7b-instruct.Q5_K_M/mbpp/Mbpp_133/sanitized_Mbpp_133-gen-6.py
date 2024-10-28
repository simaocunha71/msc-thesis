def sum_negativenum(numbers):
    negatives = [num for num in numbers if num < 0]
    return sum(negatives)