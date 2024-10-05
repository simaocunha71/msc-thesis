Here is the JavaScript code to solve the problem:

```javascript
const prodSigns = (arr) => {
  if (arr.length === 0) {
    return null;
  }
  let product = 1;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== 0) {
      product *= Math.sign(arr[i]);
      sum += Math.abs(arr[i]);
    }
  }
  return sum * product;
};
```

Explanation:

1. We first check if the array is empty. If it is, we return null.
2. We initialize two variables: `product` to store the product of all signs and `sum` to store the sum of magnitudes.
3. We loop through the array. For each number, we check if it's not zero. If it's not, we multiply the `product` by the sign of the number (using the `Math.sign()` function) and add the absolute value of the number to the `sum`.
4. Finally, we return the product of the `sum` and `product`. If the `sum` is zero, the result will be zero. If the array is empty, the result will be null. Otherwise, the result will be the sum of magnitudes multiplied by the product of all signs.