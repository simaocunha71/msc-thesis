Here is the solution to the problem:

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

The function `solution` takes a list of integers as input and returns the sum of all the odd elements that are in even positions.

We initialize a variable `sum` to 0 to keep track of the sum of the odd elements.

We then iterate through the list using a for loop. For each element in the list, we check if it is in an even position (i.e., `i % 2 === 0`) and if it is an odd number (i.e., `lst[i] % 2 !== 0`). If both conditions are true, we add the element to the `sum`.

Finally, we return the `sum`.

For example, if the input is `[5, 8, 7, 1]`, the function will return `12` because the odd elements at even positions are `5` and `7`, and their sum is `12`. If the input is `[3, 3, 3, 3, 3]`, the function will return `9` because the odd elements at even positions are `3` and `3`, and their sum is `9`. If the input is `[30, 13, 24, 321]`, the function will return `0` because there are no odd elements at even positions.