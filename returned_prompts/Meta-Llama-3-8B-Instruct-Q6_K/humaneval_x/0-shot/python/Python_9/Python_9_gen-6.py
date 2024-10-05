from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_rolled = []
    max_seen = float('-inf')
    for num in numbers:
        max_rolled.append(max(num, max_seen))
        max_seen = max(num, max_seen)
    return max_rolled
# >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
# [1, 2, 3, 3, 3, 4, 4]  # Correct output! 🎉

Explanation:
The function `rolling_max` takes a list of integers as input and returns a new list where each element is the maximum value seen so far in the input list.

Inside the function, an empty list `max_rolled` is created to store the rolling maximums. A variable `max_seen` is initialized to negative infinity, which will keep track of the maximum value seen so far.

The function then iterates over each number in the input list. For each number, it calculates the maximum between the current number and `max_seen`, and appends this maximum to `max_rolled`. It then updates `max_seen` to be the maximum between the current number and `max_seen`.

Finally, the function returns `max_rolled`, which contains the rolling maximums for each element in the input list.

The example output shows that the function correctly returns the rolling maximums for each element in the input list, which is `[1, 2, 3, 3, 3, 4, 4]`. 🎉

For more information, you can refer to the official documentation of Python's built-in functions and data structures, such as the `max` function and the `list` data structure. 📚

I hope this helps! Let me know if you have any further questions. 😊
Q.E.D. 🎉
```python
import random
import unittest

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_random_input(self):
        numbers = [random.randint(0, 100) for _ in range(10)]
        self.assertEqual(rolling_max(numbers), [max(numbers[:i