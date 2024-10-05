```js
const median = (l) => {
  let sorted = l.sort((a, b) => a - b);
  let len = sorted.length;
  if (len % 2 === 0) {
    return (sorted[len / 2 - 1] + sorted[len / 2]) / 2;
  } else {
    return sorted[(len - 1) / 2];
  }
}
```