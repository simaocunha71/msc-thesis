def return_sum(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += value
    return total


def return_sum(dictionary):
    return sum(dictionary.values())

"""
def return_sum(dictionary):
    return sum(dictionary.values())
"""
# assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
# assert return_sum({1:2, 2:4, 3:6}) == 12
# assert return_sum({'a': 100, 'b':200, 'c':300, 'd': 400}) == 1000
# assert return_sum({}) == 0


def return_sum(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total


"""
def return_sum(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total
"""
# assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
# assert return_sum({1:2, 2:4, 3:6}) == 12
# assert return_sum({'a': 100, 'b':200, 'c':300, 'd': 400}) == 1000
# assert return_sum({}) == 0


def return_sum(dictionary):
    total = 0
    for _, value in dictionary.items():
        total += value
    return total


def return_sum(dictionary):
    total = 0
    for _, value in dictionary.items():
        total += value
    return total


def return_sum(dictionary):
    return sum(dictionary.values())


def return_sum(dictionary):
    return sum(dictionary.itervalues())

def return_sum(dictionary):
    return sum(d