from typing import List

def diff_even_odd(nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            break
        i += 1
    j = 0
    while j < len(nums):
        if nums[j] % 2 == 1:
            break
        j += 1
    return nums[j] - nums[i]

# assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3
# assert diff_even_odd([1,3,5]) == 4
# assert diff_even_odd([4,6,8]) == 4

```

The above program defines a function called `diff_even_odd` that takes in a list of integers as input and returns the difference between the first even and first odd number in the list. 

The function uses two while loops to find the first even and first odd number in the list. The first while loop starts at index 0 and increments until it finds a number that is divisible by 2 (i.e., an even number). The second while loop starts at index 0 and increments until it finds a number that is not divisible by 2 (i.e., an odd number). 

Once the first even and first odd numbers are found, the function returns their difference (i.e., `nums[j] - nums[i]`). 

The program then includes a series of assert statements to test the function's behavior with different inputs. 

The expected output of the program is `True` if the assert statements pass and `False` if they fail, indicating that the function is working correctly.

```python
assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3
assert diff_even_odd([1,3,5]) == 4
assert diff_even_odd([4,6,8]) == 4
```

These assert statements verify that the `diff_even_odd` function correctly calculates the difference between the first even and first odd number in a