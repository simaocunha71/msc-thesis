To solve this problem, you can use a nested loop to iterate through each element in the list and check if there are two other distinct elements that can be added to the current element to sum to zero. Here's a step-by-step explanation of the solution:

1. Define the function `triplesSumToZero` that takes a list `l` as an argument.
2. Create an empty set `seen` to keep track of the elements we have already encountered.
3. Use a nested loop to iterate through each element `a` in the list `l`. The outer loop iterates `i` times, where `i` is the index of the current element.
4. Inside the outer loop, use a nested loop to iterate through each element `b` in the remaining part of the list `l`. The inner loop iterates `j` times, where `j` is the index of the current element in the remaining part of the list.
5. Check if the sum of the current element `a`, the element `b`, and another distinct element `c` is equal to zero. To ensure that the elements are distinct, check if `a`, `b`, and `c` are not in the `seen` set. If they are not in the set, add them to the set.
6. If the sum of `a`, `b`, and `c` is zero, return `true`. Otherwise, continue to the next iteration of the inner loop.
7. If the outer loop completes without finding a valid combination of three distinct elements, return `false`.
8. The function will return `true` if there are three distinct elements in the list that sum to zero, and `false` otherwise.

Here's the code for the solution:

```python
def triplesSumToZero(l):
    seen = set()
    for i, a in enumerate(l):
        for j, b in enumerate(l[i+1:], start=i+1):
            c = -(a + b)
            if c not in seen:
                seen.add(a)
                seen.add(b)
                seen.add(c)
                return True
    return False
```

This solution has a time complexity of O(n^2), where n is the