Here's a possible solution using Python's built-in `collections.Counter` class to count the number of zeroes and non-zeroes in the array:

```python
from collections import Counter

def zero_count(nums):
    zero_count = Counter(nums).get(0, 0)
    non_zero_count = len(nums) - zero_count
    return zero_count / non_zero_count if non_zero_count else 1
```

Explanation:
The `Counter` class is used to count the occurrences of each element in the array. The `get` method is used to get the count of zeroes (if it exists), and if it doesn't exist, it returns 0. The `non_zero_count` is calculated by subtracting the count of zeroes from the total length of the array. Finally, the ratio of zeroes to non-zeroes is calculated by dividing the count of zeroes by the count of non-zeroes, and if the count of non-zeroes is 0 (i.e., all elements in the array are zero), the ratio is set to 1 to avoid division by zero.

Note that this function assumes that the input array `nums` only contains integers.

The assertion in the original question is incorrect because the ratio of zeroes to non-zeroes in the given array `[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]` is not exactly 0.181818. The correct ratio is 0.18181818181818182, which is closer to 1/5.

Here's a breakdown of the calculation:
- The array `[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]` has 2 zeroes and 12 non-zeroes.
- The ratio of zeroes to non-zeroes is `(2 / 12) = 1 / 6 ≈ 0.1666