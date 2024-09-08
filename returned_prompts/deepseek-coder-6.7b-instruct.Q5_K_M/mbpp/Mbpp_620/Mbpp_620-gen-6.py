This problem can be solved using the concept of dynamic programming.

The idea is to sort the array in increasing order. Then, for every number, we check all the smaller numbers and try to extend the longest subset ending at that number. 

Finally, we return the maximum length found.

Here is the Python code which does the same.

```python
def largest_subset(lst):
    lst.sort()
    n = len(lst)
    T = [1]*n
    for i in range(1, n):
        for j in range(i):
            if lst[i] % lst[j] == 0:
                T[i] = max(T[i], T[j] + 1)
    return max(T)

print(largest_subset([ 1, 3, 6, 13, 17, 18 ]))  # Output: 4
```
In the above code, `T[i]` stores the length of the longest subset ending at `lst[i]`. For every `lst[i]`, we are iterating over `lst[0 ... i-1]` and if `lst[i]` is divisible by `lst[j]`, we extend the longest subset ending at `lst[j]` by `lst[i]`.

The time complexity of this solution is O(n^2) where n is the size of the list.

In the example provided, the longest subset is `[1, 3, 6, 18]` which has size 4.
"""

def largest_subset(lst):
    lst.sort()
    n = len(lst)
    T = [1]*n
    for i in range(1, n):
        for j in range(i):
            if lst[i] % lst[j] == 0:
                T[i] = max(T[i], T[j] + 1)
    return max(T)

print(largest_subset([ 1, 3, 6, 13, 17, 18 ]))  # Output: 4
```
"""
