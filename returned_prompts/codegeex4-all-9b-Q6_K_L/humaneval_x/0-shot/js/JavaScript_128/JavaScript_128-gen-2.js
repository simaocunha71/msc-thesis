```js
const prodSigns = (arr) => {
  if (!arr.length) return null;
  let prod = 1, sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) prod *= -1;
    else if (arr[i] === 0) prod = 0;
    sum += Math.abs(arr[i]);
  }
  return prod * sum;
}
```