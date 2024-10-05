```js
const histogram = (test) => {
  if (test.length === 0) return {};
  const arr = test.split(" ");
  const counts = {};
  for (let i = 0; i < arr.length; i++) {
    if (counts[arr[i]]) {
      counts[arr[i]]++;
    } else {
      counts[arr[i]] = 1;
    }
  }
  let maxCount = 0;
  for (let key in counts) {
    if (counts[key] > maxCount) {
      maxCount = counts[key];
    }
  }
  const result = {};
  for (let key in counts) {
    if (counts[key] === maxCount) {
      result[key] = maxCount;
    }
  }
  return result;
}
```
