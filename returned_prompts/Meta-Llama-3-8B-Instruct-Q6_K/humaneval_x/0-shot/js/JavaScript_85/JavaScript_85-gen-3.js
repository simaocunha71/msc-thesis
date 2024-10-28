Here is a JavaScript function that solves the problem:

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

This function iterates over the list, starting from the second element (index 1), and checks if the current element is even (using the modulus operator `%` to check if the remainder of the division by 2 is 0). If it is even, it adds it to the sum. Finally, it returns the sum.