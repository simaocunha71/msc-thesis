The logic to solve this problem is to use a set to keep track of the numbers that we have seen so far. For each number in the list, we check if -num exists in the set. If it does, we return true, since we have found two distinct elements that sum to zero. If it doesn't, we add the current element to the set.

In Python, we can use the built-in set data structure to keep track of the elements. Here's a step-by-step breakdown of the solution:

1. Initialize an empty set called 'seen' to keep track of the elements.
2. Iterate through each number in the list 'l'.
3. For each number, check if -num exists in the 'seen' set. If it does, return true since we have found two distinct elements that sum to zero.
4. If -num does not exist in the 'seen' set, add the current element to the 'seen' set.
5. If we have iterated through all the elements in the list and haven't found any pair that sums to zero, return false.

Here's the Python code that implements the above logic:

```python
def pairsSumToZero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
```

You can use this code as a reference to implement the logic in your chosen programming language.

Note: The time complexity of this solution is O(n), where n is the length of the input list. This is because we iterate through the list once and perform a constant time lookup and insertion in the set for each element.

I hope this helps! Let me know if you have any more questions.

*/



/*
  pairsSumToZero takes a list of integers as an input.
  it returns true if there are two distinct elements in the list that
  sum to zero, and false otherwise.
  >>> pairsSumToZero([1, 3, 5, 0])
  false
  >>> pairsSumToZero([1, 3, -2, 1])
  false
  >>> pairsSumToZero([1, 2, 3, 7])
  false
