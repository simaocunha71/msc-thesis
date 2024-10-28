```javascript
const prodSigns = (arr) => {
  if (arr.length == 0) return null;
  let product = 1;
  let signProduct = 1;
  for (let i = 0; i < arr.length; i++) {
    product *= Math.abs(arr[i]);
    signProduct *= (arr[i] > 0) ? 1 : -1;
  }
  return product * signProduct;
}
```