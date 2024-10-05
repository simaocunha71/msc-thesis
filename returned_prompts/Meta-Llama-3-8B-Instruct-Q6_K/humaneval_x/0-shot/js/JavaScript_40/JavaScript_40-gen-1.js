Here is a Python solution for the problem:

```python
def triplesSumToZero(l):
    l = set(l)
    for i in l:
        for j in l:
            if i + j in l:
                return True
    return False
```

In this solution, we first convert the list to a set for efficient lookup. Then we iterate over each pair of elements in the set. If the sum of the pair is also in the set, we return True. If no such pair is found after iterating over all pairs, we return False. This solution has a time complexity of O(n^2) where n is the length of the input list.

Alternatively, we can use a hash map to store the elements we have seen so far and their complements. Here is the Python code for this approach:

```python
def triplesSumToZero(l):
    seen = {}
    for num in l:
        if -num in seen:
            return True
        seen[num] = True
    return False
```

This solution has a time complexity of O(n) and a space complexity of O(n). It works by iterating over the list and for each element, it checks if its complement (i.e., the number that would sum to zero) is in the seen dictionary. If it is, it returns True. If it is not, it adds the current element to the seen dictionary. If it finishes iterating over the list without finding a triplet that sums to zero, it returns False. This solution is more efficient than the previous one for large input lists.