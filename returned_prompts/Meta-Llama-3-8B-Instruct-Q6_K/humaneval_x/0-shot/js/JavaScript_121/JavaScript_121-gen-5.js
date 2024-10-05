Here is the solution for the problem:

```javascript
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```


Explanation:

*   We initialize a variable `sum` to 0, which will be used to store the sum of the odd elements in even positions.
*   We iterate through the list using a for loop, keeping track of the current index `i`.
*   We check if the current index `i` is even (using the condition `i % 2 === 0`) and if the element at that index is odd (using the condition `lst[i] % 2 !== 0`).
*   If both conditions are true, we add the element to the `sum`.
*   Finally, we return the `sum` at the end of the function.

This solution correctly identifies the odd elements in even positions and returns their sum. It works for any non-empty list of integers.