Here is a JavaScript function that fulfills the requirements:
```javascript
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      if (lst.filter(x => x === lst[i]).length > 1) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
```
Here's an explanation of how the function works:

1. We iterate through the list using a for loop, comparing each element to the next one.
2. If an element is greater than or equal to the next one, we check if there are any duplicates of that element in the list. If there are, we return `false`, because the list is not sorted.
3. If an element is not greater than or equal to the next one, we return `false`, because the list is not sorted.
4. If we reach the end of the loop without returning `false`, we return `true`, because the list is sorted.

You can test this function with the examples provided in the problem statement to see that it produces the correct results.