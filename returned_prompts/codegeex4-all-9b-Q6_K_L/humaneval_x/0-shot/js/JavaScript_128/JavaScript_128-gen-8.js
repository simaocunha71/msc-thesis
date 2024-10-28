```javascript
const prodSigns = (arr) => {
  if (!arr.length) return null;
  let sign = 1;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += Math.abs(arr[i]);
    sign *= Math.sign(arr[i]);
  }
  return sum * sign;
}
```
