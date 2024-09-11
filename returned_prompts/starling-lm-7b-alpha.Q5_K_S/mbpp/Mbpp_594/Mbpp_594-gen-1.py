from typing import List

def diff_even_odd(nums: List[int]) -> int:
    odd_nums = [n for n in nums if n % 2 != 0]
    even_nums = [n for n in nums if n % 2 == 0]
    if len(odd_nums) > 0 and len(even_nums) > 0:
        return odd_nums[0] - even_nums[0]
    else:
        raise ValueError('List must contain at least one odd and one even number')


# assert diff_even_odd([1,3,5,7,4,1,6,8]) == 3
# assert diff_even_odd([1,3,5,7]) == None
# assert diff_even_odd([4,1,6,8]) == 2
# assert diff_even_odd([0,1,2,3,4,5,6,7,8]) == 0


```

```
def diff_even_odd(nums: List[int]) -> int:
    odd_nums = [n for n in nums if n % 2 != 0]
    even_nums = [n for n in nums if n % 2 == 0]
    if len(odd_nums) > 0 and len(even_nums) > 0:
        return odd_nums[0] - even_nums[0]
    else:
        raise ValueError('List must contain at least one odd and one even number')
```
This function `diff_even_odd` uses list comprehension to create two separate lists of odd and even numbers from the given list of integers. It then checks if both odd and even lists are not empty. If they are not empty, it returns the difference between the first odd and first even number. Otherwise, it raises a `ValueError` with a message indicating that the list must contain at least one odd and one even number.

To use this function, you can call it with a list of integers, like in the example below:

```python
result = diff_even_odd([1, 3, 5, 7,