```js
const f = (n) => {
  if (n === 0) return [];
  if (n === 1) return [1];
  let arr = [1];
  for (let i = 1; i < n; i++) {
    if (i % 2 === 0) {
      arr[i] = arr[i - 1] * i;
    } else {
      arr[i] = 0;
      for (let j = 1; j <= i; j++) {
        arr[i] += j;
      }
    }
  }
  return arr;
};
```
