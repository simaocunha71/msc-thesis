Here is a JavaScript function that solves the problem:
```javascript
const isSorted = (lst) => {
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] <= lst[i - 1]) {
      if (lst.includes(lst[i], i + 1)) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
```
Here's an explanation of the code:

1. We iterate through the list using a for loop, starting from the second element (index 1).
2. For each element, we check if it is less than or equal to the previous element. If it is, we continue to the next element.
3. If the current element is greater than the previous element, we immediately return `false`, as the list is not sorted.
4. If we reach the end of the loop without returning `false`, we return `true`, indicating that the list is sorted.
5. To check for duplicates, we use the `includes()` method with a start index of `i + 1` to search for the current element in the rest of the list. If we find a duplicate, we return `false`.

You can test the function with the examples provided in the problem statement to verify its correctness.