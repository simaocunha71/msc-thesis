```js
const prodSigns = (arr) => {
  if (arr.length === 0) return null;
  let prod = 1;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += Math.abs(arr[i]);
    prod *= Math.sign(arr[i]);
  }
  return sum * prod;
}
```
