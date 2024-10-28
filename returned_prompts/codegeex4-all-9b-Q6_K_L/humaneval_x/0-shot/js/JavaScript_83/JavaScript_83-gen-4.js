```js
const startsOneEnds = (n) => {
  let count = 0;
  for (let i = 1; i <= 9; i++) {
    if (i.toString().startsWith('1')) {
      count++;
    }
  }
  if (n === 1) return count;
  let totalNumbers = Math.pow(10, n - 2);
  return count * totalNumbers * 2;
};
```
