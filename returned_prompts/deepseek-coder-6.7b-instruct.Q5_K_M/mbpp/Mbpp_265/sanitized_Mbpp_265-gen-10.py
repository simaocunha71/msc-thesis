import numpy as np
def list_split(l, n):
    return [list(x) for x in np.array_split(l, len(l) // n)]