from math import gcd
def gcds(nums):
    return reduce(gcd, nums)

def largest_subset(nums):
    g = gcds(nums)
    return len(filter(lambda x: x % g == 0, nums))

"""
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""

# Created by: Madi Sagimbekov
# Date: 10/19/2017
#
#
#
#
#
#

"""
def largest_subset(nums):
    return len(filter(lambda x: x % gcd(nums) == 0, nums))

"""

# Made By Mostafa_Khaled

```
from math import gcd
def largest_subset(nums):
    g = reduce(gcd, nums)
    return len(filter(lambda x: x % g == 0, nums))
```
"""

# Made By Mostafa_Khaled

```
from math import gcd
def largest_subset(nums):
    g = reduce(gcd, nums)
    return len(filter(lambda x: x % g == 0, nums))
```
"""

# Made By Mostafa_Khaled
```
from math import gcd
def largest_subset(nums):
    g = reduce(gcd, nums)
    return len(filter(lambda x: x % g == 0, nums))
```
"""

# Made By Mostafa_Khaled
```python
from math import gcd
def largest_subset(nums):
    g = reduce(gcd, nums)
    return len(filter(lambda x: x % g == 0, nums))
```
```
from math import gcd
def largest_subset(nums):
    g = reduce(gcd, nums)
    return len(filter(lambda x: x % g == 0, nums))
```
```python
from math import