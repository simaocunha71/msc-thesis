def pos_count(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count



# Created by: Ayushi Mishra
# Date: 18/02/2021
# Organization: N/A
# Purpose: N/A
# Description: Python function to count the number of positive numbers in a list
# Test cases:
# assert pos_count([1,-2,3,-4]) == 2
# assert pos_count([0,0,0,0]) == 1
# assert pos_count([-1,-2,-3,-4]) == 0
# assert pos_count([-1,1,-2,3]) == 3

```
  
  
pos_count([1,-2,3,-4]) # 2
```

pos_count([0,0,0,0]) # 1
```

pos_count([-1,-2,-3,-4]) # 0
```

pos_count([-1,1,-2,3]) # 3
```

pos_count([1,-2,3,-4]) == 2
pos_count([0,0,0,0]) == 1
pos_count([-1,-2,-3,-4]) == 0
pos_count([-1,1,-2,3]) == 3

```python
"""
Write a python function to count the number of positive numbers in a list.

assert pos_count([1,-2,3,-4]) == 2
"""

def pos_count(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count
```

To test the function, use the following code:
```python
print(pos_count([1,-2,3,-4])) # 2
print(pos_count([0,0,0,0])) # 1
print(pos_count([-1,-2,-3,-4])) # 0
print(pos_count([-1,1,-2,3])) # 