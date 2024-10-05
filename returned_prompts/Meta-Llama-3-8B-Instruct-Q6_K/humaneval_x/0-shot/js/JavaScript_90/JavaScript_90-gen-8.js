Here is the solution:
```
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  lst.sort((a, b) => a - b);
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] !== lst[i - 1]) return lst[i];
  }
  return null;
};
```
Here's an explanation of the solution:

1. First, we check if the list has less than 2 elements. If it does, we return null, as there is no 2nd smallest element.
2. We sort the list in ascending order.
3. We then iterate through the sorted list, starting from the 2nd element (index 1).
4. For each element, we check if it's different from the previous element. If it is, we return that element, as it's the 2nd smallest.
5. If we reach the end of the list without finding a different element, it means the list has only one unique element, so we return null.

You can test this function with the provided examples to see that it returns the correct results.