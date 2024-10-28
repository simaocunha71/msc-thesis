```js
const willItFly = (q, w) => {
  let sum = 0;
  for (let i = 0; i < q.length; i++) {
    sum += q[i];
  }
  if (sum > w) {
    return false;
  }
  if (q.length % 2 == 0) {
    return false;
  }
  for (let i = 0; i < Math.floor(q.length / 2); i++) {
    if (q[i] != q[q.length - i - 1]) {
      return false;
    }
  }
  return true;
};
```
