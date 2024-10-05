```js
const prodSigns = (arr) => {
  if (!arr.length) return null;
  let sign = 1;
  let magnitudeSum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) sign *= -1;
    magnitudeSum += Math.abs(arr[i]);
  }
  return sign * magnitudeSum;
}
```
