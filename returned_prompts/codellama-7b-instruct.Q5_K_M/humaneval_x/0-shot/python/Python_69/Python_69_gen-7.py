
def search(lst):
    max_frequency = -1
    max_number = -1
    for number in lst:
        frequency = lst.count(number)
        if frequency > number and frequency > max_frequency:
            max_frequency = frequency
            max_number = number
    return max_number if max_number > 0 else -1
