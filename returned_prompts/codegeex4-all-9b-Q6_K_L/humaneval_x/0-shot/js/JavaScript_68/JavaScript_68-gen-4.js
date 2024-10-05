```js
const pluck = (arr) => {
  let min = Infinity;
  let minIdx = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < min) {
      min = arr[i];
      minIdx = i;
    }
  }
  if (minIdx === -1) return [];
  return [min, minIdx];
};
```