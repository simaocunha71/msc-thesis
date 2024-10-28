Here is a solution using JavaScript:

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

This function iterates over the input list, checking if each element is in an even position (i.e., `i % 2 === 0`) and if the element is odd (i.e., `lst[i] % 2 !== 0`). If both conditions are true, it adds the element to the sum. Finally, it returns the sum.