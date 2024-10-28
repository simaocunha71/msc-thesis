```js
const search = (lst) => {
  if (lst.length === 0) return -1;
  let max = -1;
  let frequencyMap = {};
  for (let num of lst) {
    frequencyMap[num] = (frequencyMap[num] || 0) + 1;
    if (num > max) max = num;
  }
  for (let i = max; i > 0; i--) {
    if (frequencyMap[i] >= i) return i;
  }
  return -1;
}
```