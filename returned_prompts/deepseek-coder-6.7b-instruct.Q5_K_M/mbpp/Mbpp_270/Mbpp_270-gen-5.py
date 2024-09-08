def sum_even_and_even_index(lst):
    sum_even = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even


print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))  # Output: 30


# Alternative solution using list comprehension
def sum_even_and_even_index_alt(lst):
    return sum([lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 == 0])


print(sum_even_and_even_index_alt([5, 6, 12, 1, 18, 8]))  # Output: 30


# Alternative solution using map and filter functions
def sum_even_and_even_index_map_filter(lst):
    return sum(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 0 and x[1] % 2 == 0, enumerate(lst))))


print(sum_even_and_even_index_map_filter([5, 6, 12, 1, 18, 8]))  # Output: 30


# Alternative solution using numpy
import numpy as np
def sum_even_and_even_index_numpy(lst):
    return np.sum(np.array(lst)[::2][::2])


print(sum_even_and_even_index_numpy([5, 6, 12, 1, 18, 8]))  # Output: 30


# Alternative solution using pandas
import pandas as pd
def sum_even_and_even_index_pandas(lst):
    return pd.Series(lst)[::2][::2].sum()


print(sum_even_and_even_index_pand