```js
const sumSquares = (lst) => {
  if (lst.length === 0) return 0;
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) sum += lst[i] * lst[i];
    if (i % 4 === 0 && i % 3 !== 0) sum += lst[i] * lst[i] * lst[i];
  }
  return sum;
}
```