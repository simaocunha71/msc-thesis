
def eat(number, need, remaining):
    return [number + remaining + need, remaining - (need - remaining) if need > remaining else 0]

# eat(5, 6, 10) -> [11, 4]
# eat(4, 8, 9) -> [12, 1]
# eat(1, 10, 10) -> [11, 0]
# eat(2, 11, 5) -> [7, 0]







```
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:00:14 2019

@author: LENOVO
"""

def eat(number, need, remaining):
    return [number + remaining + need, remaining - (need - remaining) if need > remaining else 0]

# eat(5, 6, 10) -> [11, 4]
# eat(4, 8, 9) -> [12, 1]
# eat(1, 10, 10) -> [11, 0]
# eat(2, 11, 5) -> [7, 0]
```