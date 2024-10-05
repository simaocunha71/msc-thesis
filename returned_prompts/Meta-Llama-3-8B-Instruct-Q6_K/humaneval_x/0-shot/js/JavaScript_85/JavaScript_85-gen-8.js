Here is the JavaScript function that solves the problem:

```javascript
const add = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```

In this function, we initialize a variable `sum` to 0. Then we loop through the list `lst` starting from the second element (index 1) and incrementing the index by 2 in each iteration (to consider only the elements at odd indices). If the current element is even (i.e., `lst[i] % 2 === 0`), we add it to the `sum`. Finally, we return the `sum`.

For example, if we call `add([4, 2, 6, 7])`, the function will return `2`, which is the sum of the even elements at odd indices (2 and 6).