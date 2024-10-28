import numpy as np
import pandas as pd
def sum_even_and_even_index(lst):
    sum_even = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even