def diff_even_odd(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0 or len(odd) == 0:
        return 0
    else:
        return even[0] - odd[0]





# Created by: Ayush Kumar
# Date: 23/06/2020
# Time: 20:58
# File Name: main.py

```
def diff_even_odd(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 0 or len(odd) == 0:
        return 0
    else:
        return even[0] - odd[0]

# Created by: Ayush Kumar
# Date: 23/06/2020
# Time: 20:58
# File Name: main.py

```


# Tests
# Test case 1
print(diff_even_odd([1,3,5,7,4,1,6,8]))  # Expected: 3
# Test case 2
print(diff_even_odd([1,3,5,7,4,8,6,1]))  # Expected: -3
# Test case 3
print(diff_even_odd([1,3,5,7,4,8,6]))  # Expected: 0
# Test case 4
print(diff_even_odd([]))  # Expected: 0
# Test case 5
print(diff_even_odd([1,3,5,7,4,1,6,8,9,10]))  # Expected: 3
```

```python
# Created by: Ayush Kumar
# Date: 23/06/2020