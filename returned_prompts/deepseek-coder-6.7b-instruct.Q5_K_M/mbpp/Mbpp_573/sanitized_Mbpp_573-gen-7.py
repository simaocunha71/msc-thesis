from functools import reduce
from math import prod
import numpy as np
import pandas as pd
from functools import reduce
import numpy as np
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product