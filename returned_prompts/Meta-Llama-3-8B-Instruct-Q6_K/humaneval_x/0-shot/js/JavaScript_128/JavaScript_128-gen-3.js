```
const prodSigns = (arr) => {
  if (!arr.length) return null;

  let productOfSigns = 1;
  let sumOfMagnitudes = 0;

  for (let num of arr) {
    if (num === 0) {
      return 0;
    }
    productOfSigns *= Math.sign(num);
    sumOfMagnitudes += Math.abs(num);
  }

  return productOfSigns * sumOfMagnitudes;
};
```


This solution iterates through the input array, keeping track of the product of signs and the sum of magnitudes. If the array is empty, it returns null. If any number in the array is 0, it returns 0 because the product of signs cannot be calculated. Finally, it returns the product of signs and the sum of magnitudes.

The `Math.sign()` function is used to get the sign of a number (1 for positive, -1 for negative, and 0 for zero). The `Math.abs()` function is used to get the magnitude of a number. The `*=` operator is used to multiply the product of signs by the sign of the current number, and the `+=` operator is used to add the magnitude of the current number to the sum of magnitudes.