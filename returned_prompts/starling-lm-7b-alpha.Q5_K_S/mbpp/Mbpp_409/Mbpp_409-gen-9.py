"""
def min_product_tuple(list_tuple):
    list_tuple.sort(key = lambda x : x[0]*x[1])
    return list_tuple[0][0]*list_tuple[0][1]

# Test
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] ))
"""

# Solution

def min_product_tuple(list_tuple):
    list_tuple.sort(key = lambda x : x[0]*x[1])
    return list_tuple[0][0]*list_tuple[0][1]

# Test
print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] ))
```
