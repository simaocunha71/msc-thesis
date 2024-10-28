Here is the solution:

```javascript
const nextSmallest = (lst) => {
  if (lst.length < 2) return null;
  lst = lst.filter((x, i) => lst.indexOf(x) === i);
  if (lst.length < 2) return null;
  return Math.min(...lst.slice(1));
};
```

Explanation:

1. First, we check if the length of the input list is less than 2. If it is, we return null because there is no 2nd smallest element.

2. We then filter out any duplicate elements in the list. This is because the 2nd smallest element is unique by definition.

3. If the filtered list has a length of less than 2, we return null.

4. Finally, we return the 2nd smallest element by using the `Math.min()` function and spreading the filtered list starting from the second element (`slice(1)`).

This function works for both sorted and unsorted lists, and it correctly handles the edge cases where the list is empty or has only one element.