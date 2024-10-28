def return_sum(dictionary):
    if not dictionary:
        return 0
    total = 0
    for value in dictionary.values():
        total += value
    return total