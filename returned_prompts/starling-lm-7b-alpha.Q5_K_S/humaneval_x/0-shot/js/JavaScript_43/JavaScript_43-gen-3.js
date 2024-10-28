To solve this problem, we can use a Set to keep track of the elements we've seen so far. We'll iterate through the list, checking if the negation of each number is in the set. If it is, we found a pair that sums to zero, so we return true. Otherwise, we add the current number to the set and continue. If we finish the list without finding a pair, we return false.

Here's some sample input to test the function:

pairsSumToZero([1, 3, 5, 0])  # false
pairsSumToZero([1, 3, -2, 1]) # false
pairsSumToZero([1, 2, 3, 7]) # false
pairsSumToZero([2, 4, -5, 3, 5, 7]) # true
pairsSumToZero([1]) # false

The function can be implemented as follows:

```python
def pairsSumToZero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
```

This implementation has a time complexity of O(n), where n is the length of the input list.

Here's a step-by-step walkthrough of the function's execution for the first sample input, [1, 3, 5, 0]:

1. Initialize an empty set called `seen`.
2. Iterate through the list:
   - For the first element, 1, there is no -1 in the set, so we add 1 to the set and continue.
   - For the second element, 3, there is no -3 in the set, so we add 3 to the set and continue.
   - For the third element, 5, there is no -5 in the set, so we add 5 to the set and continue.
   - For the fourth element, 0, there is no -0 in the set, so we add 0 to the set and continue.
3. After iterating through the entire list, there are no pairs of distinct elements that sum to zero, so we return False.

For the second sample input, [1, 