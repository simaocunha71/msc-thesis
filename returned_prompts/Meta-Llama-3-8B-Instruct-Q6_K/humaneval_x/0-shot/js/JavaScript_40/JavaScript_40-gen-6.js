Here is a Python solution:
```python
def triplesSumToZero(l):
    l.sort()
    for i in range(len(l) - 2):
        left, right = i + 1, len(l) - 1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return True
    return False
```
Here's a breakdown of the solution:

1. First, we sort the list. This is because we're looking for three distinct elements that sum to zero, and sorting the list helps us find these elements more efficiently.
2. We then iterate through the list, considering each element as the first element of the triple.
3. For each element, we use two pointers, `left` and `right`, to search for the other two elements. `left` starts at the next element after the current one, and `right` starts at the end of the list.
4. We calculate the sum of the three elements (`l[i] + l[left] + l[right]`) and check if it's less than zero. If it is, we increment `left` to make the sum larger. If it's greater than zero, we decrement `right` to make the sum smaller. If the sum is exactly zero, we return `True`.
5. If we reach the end of the loop without finding a triple that sums to zero, we return `False`. This means that there are no three distinct elements in the list that sum to zero.

Note that this solution has a time complexity of O(n^2), where n is the length of the input list. This is because we're using two pointers to search for the other two elements, and this search takes O(n) time. However, this solution is still quite efficient for small to medium-sized lists. If you need a more efficient solution for very large lists, you may want to consider using a more advanced algorithm, such as a hash table or a balanced binary search tree.