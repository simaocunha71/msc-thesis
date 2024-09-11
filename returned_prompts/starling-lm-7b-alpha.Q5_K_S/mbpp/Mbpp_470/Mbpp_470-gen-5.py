def add_pairwise(tuple_):
    '''
    Find the pairwise addition of the neighboring elements of the given tuple.
    '''
    result = []
    for i in range(len(tuple_)-1):
        result.append(tuple_[i]+tuple_[i+1])
    result.append(tuple_[len(tuple_)-1]+tuple_[0])
    return tuple(result)

# Test
print(add_pairwise((1, 5, 7, 8, 10))) # (6, 12, 15, 18)
























# Created by: Akshay



# Last Modified: 29/May/2021

# -*- coding: utf-8 -*-
"""



"""

import sys
from collections import Counter
from collections import OrderedDict

def add_pairwise(tuple_):
    '''
    Find the pairwise addition of the neighboring elements of the given tuple.
    '''
    result = []
    for i in range(len(tuple_)-1):
        result.append(tuple_[i]+tuple_[i+1])
    result.append(tuple_[len(tuple_)-1]+tuple_[0])
    return tuple(result)

# Test
print(add_pairwise((1, 5, 7, 8, 10))) # (6, 12, 15, 18)
























# Created by: Akshay



# Last Modified: 29/May/2021

# -*- coding: utf-8 -*-
"""



"""

import sys
from collections import Counter
from collections import OrderedDict

def add_pairwise(tuple_):
    '''
    Find the pairwise addition of the neighboring elements of the given tuple.
    '''
    result = []
    for i in range(len(tuple_)-1):
        result.append(tuple_[i]+tuple_[i+1