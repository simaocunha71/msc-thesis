```javascript
const prodSigns = (arr) => {
  if (!arr.length) return null;
  let product = 1;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      product *= -1;
    } else if (arr[i] === 0) {
      return 0;
    }
    sum += Math.abs(arr[i]);
  }
  return product * sum;
}
```
