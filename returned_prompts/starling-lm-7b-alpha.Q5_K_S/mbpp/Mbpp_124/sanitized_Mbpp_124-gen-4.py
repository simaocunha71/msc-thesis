import math
from functools import reduce
def angle_complex(a, b):
    return reduce(lambda x, y: complex(x, y), [a, b])