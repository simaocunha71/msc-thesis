# Here are some solutions to this problem
# Solution 1:
def sum_squares(lst):
    lst = [int(i) for i in lst]
    return sum([i**2 for i in lst])

# Solution 2:
def sum_squares(lst):
    lst = [int(i) for i in lst]
    return sum(i**2 for i in lst)

# Solution 3:
from math import ceil
def sum_squares(lst):
    return sum(ceil(i)**2 for i in lst)

# Test cases
print(sum_squares([1,2,3]))  # Expected: 14
print(sum_squares([1,4,9]))  # Expected: 98
print(sum_squares([1,3,5,7]))  # Expected: 84
print(sum_squares([1.4,4.2,0]))  # Expected: 29
print(sum_squares([-2.4,1,1]))  # Expected: 6

# More test cases
print(sum_squares([]))  # Expected: 0
print(sum_squares([100]))  # Expected: 10000
print(sum_squares([-2.4,-1,1]))  # Expected: 6
print(sum_squares([0.1,0.2,0.3]))  # Expected: 14

# Another test
print(sum_squares(list(range(1, 11))))  # Expected: 385

# Stress test
print(sum_squares(list(range(0, 100000))))  # Expected: 33333333333333333333












```

  
```

```

  






```

```

```

```

```

