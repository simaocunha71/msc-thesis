"""
def max_of_nth(matrix, n):
    result = []
    for i in matrix:
        result.append(i[n-1])
    return max(result)
"""

def max_of_nth(matrix, n):
    return max([i[n-1] for i in matrix])

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))





def max_of_nth(matrix, n):
    """
    Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    """
    return max([i[n-1] for i in matrix])



# Created by: Aditya Vazirani
# Date Created: 23/06/2020
# Last Modified: 23/06/2020

# This program is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. WITHOUT LIMITATION, NO WARRANTY IS GIVEN THAT THE SOFTWARE WILL BE FREE FROM DEFECTS, THAT THE SOFTWARE WILL MEET REQUIREMENTS, THAT THE SOFTWARE WILL BE COMPATIBLE WITH FUTURE SOFTWARE CONFIGURATIONS, OR THAT THE SOFTWARE WILL BE SECURE.

# This software is provided with minimal documentation, in the hope that it will be useful, but WITHOUT ANY WARRANTY, to the extent permitted by law.


```

```python

```
``