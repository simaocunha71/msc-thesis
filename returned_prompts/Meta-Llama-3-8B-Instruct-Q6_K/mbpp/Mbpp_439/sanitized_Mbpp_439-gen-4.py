def multiple_to_single(lst):
    result = 0
    for num in lst:
        result = result * 10 + num
    return result