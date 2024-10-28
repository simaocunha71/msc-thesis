

def get_positive(l: list):
    return [i for i in l if i > 0]


print(get_positive([-1, 2, 3, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))


# Alternative solution using list comprehension
def get_positive(l: list):
    return [num for num in l if num > 0]


print(get_positive([-1, 2, 3, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))


# Alternative solution using filter function
def get_positive(l: list):
    return list(filter(lambda num: num > 0, l))


print(get_positive([-1, 2, 3, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))


# Alternative solution using traditional loop
def get_positive(l: list):
    positive_list = []
    for num in l:
        if num > 0:
            positive_list.append(num)
    return positive_list


print(get_positive([-1, 2, 3, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))


# Alternative solution using traditional loop with built-in 'filter()' function
def get_positive(l: list):
    return list(filter(lambda num: num > 0, l))


print(get_positive([-1, 2, 3, -4, 5, 6]))
print(get_positive([5, 3