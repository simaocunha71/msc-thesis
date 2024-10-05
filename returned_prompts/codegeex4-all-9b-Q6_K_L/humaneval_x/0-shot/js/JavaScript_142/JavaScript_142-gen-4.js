```js
const sumSquares = (lst) => {
  return lst.reduce((sum, num, i) => {
    if (i % 3 === 0) {
      sum += num * num;
    } else if (i % 4 === 0) {
      sum += num * num * num;
    } else {
      sum += num;
    }
    return sum;
  }, 0);
}
```