    import numpy as np
    numbers = np.array(numbers)
    min_val = np.min(numbers)
    max_val = np.max(numbers)
    rescaled = (numbers - min_val) / (max_val - min_val)
    return rescaled.tolist()  # convert numpy array to list
    # Alternative solution using built-in Python functions:
    # min_val = min(numbers)
    # max_val = max(numbers)
    # return [(x - min_val) / (max_val - min_val) for x in numbers]  # list comprehension
    # or
    # return [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]  # list comprehension
    # or
    # numbers_min = min(numbers)
    # numbers_max = max(numbers)
    # return [((x - numbers_min) / (numbers_max - numbers_min)) for x in numbers]  # list comprehension
    # or
    # import statistics
    # return [(x - statistics.fmin(numbers)) / (statistics.fmax(numbers) - statistics.fmin(numbers)) for x in numbers]  # list comprehension
    # or
    # import math
    # return [math.map(lambda x: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers)]  # lambda function
    # or
    # import operator
    # return [operator.map(lambda x: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers)]  # lambda function
    # or
    # import functools
    # return [functools.reduce(lambda x, y: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers)]  # lambda function
    # or
    # import itertools
    # return [itertools.reduce(lambda x, y: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers)]  # lambda function
    # or
    # return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]  # list comprehension
    # or
    # return [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]  # list comprehension
    # or
    # return [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]  # list comprehension
    # or
    # return [(x - min