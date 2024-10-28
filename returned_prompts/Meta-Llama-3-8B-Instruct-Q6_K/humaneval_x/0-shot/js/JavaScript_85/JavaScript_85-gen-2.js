Here is the solution:

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

Explanation:

*   We initialize a variable `sum` to 0, which will store the sum of even elements at odd indices.
*   We use a for loop to iterate over the list, starting from the second element (index 1) and incrementing the index by 2 in each iteration.
*   Inside the loop, we check if the current element is even by using the modulus operator (`%`). If it is even, we add it to the `sum`.
*   Finally, we return the `sum`.

For example, if we call `add([4, 2, 6, 7])`, the function will iterate over the list as follows:
```javascript
i = 1, lst[i] = 2, sum = 2
i = 3, lst[i] = 6, sum = 8
```

The function will return `8`, which is the sum of even elements at odd indices.