def filter_oddnumbers(lst):
    result = []
    for num in lst:
        if num % 2 != 0:
            result.append(num)
    return result