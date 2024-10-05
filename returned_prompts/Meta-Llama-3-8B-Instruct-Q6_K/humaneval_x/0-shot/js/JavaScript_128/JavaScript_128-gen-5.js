Here is a JavaScript solution for the problem:

```javascript
const prodSigns = (arr) => {
  if (!arr.length) return null;

  let signProduct = 1;
  let sumOfMagnitudes = 0;

  for (let num of arr) {
    if (num === 0) {
      return 0;
    }
    signProduct *= Math.sign(num);
    sumOfMagnitudes += Math.abs(num);
  }

  return signProduct * sumOfMagnitudes;
};
```

This function first checks if the array is empty. If it is, it returns null. Then it initializes two variables: `signProduct` to 1 and `sumOfMagnitudes` to 0. It then loops through each number in the array. If the number is 0, it returns 0 because the sum of magnitudes is undefined for an array containing 0. If the number is not 0, it updates `signProduct` by multiplying it by the sign of the number (1 for positive numbers, -1 for negative numbers, and 0 for 0), and updates `sumOfMagnitudes` by adding the absolute value of the number. Finally, it returns the product of `signProduct` and `sumOfMagnitudes`.