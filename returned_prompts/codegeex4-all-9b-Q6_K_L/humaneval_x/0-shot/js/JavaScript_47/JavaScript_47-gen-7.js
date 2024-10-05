```js
const median = (l) => {
  var sorted = l.sort((a, b) => a - b);
  var len = sorted.length;
  var middle = Math.floor(len / 2);

  if (len % 2 === 0) {
    return (sorted[middle - 1] + sorted[middle]) / 2;
  } else {
    return sorted[middle];
  }
}
```