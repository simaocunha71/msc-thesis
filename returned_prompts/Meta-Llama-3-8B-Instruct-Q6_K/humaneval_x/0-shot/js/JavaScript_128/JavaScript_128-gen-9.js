Here is a JavaScript function that meets the requirements:
```
const prodSigns = (arr) => {
  if (arr.length === 0) {
    return null;
  }
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
Here's an explanation of the code:

1. We first check if the input array is empty. If it is, we return null.
2. We initialize two variables: `productOfSigns` to keep track of the product of all signs in the array, and `sumOfMagnitudes` to keep track of the sum of magnitudes of all numbers in the array.
3. We iterate through the array using a for...of loop. For each number, we check if it's zero. If it is, we return zero immediately, since the product of signs is undefined for an array containing zero.
4. We update `productOfSigns` by multiplying it by the sign of the current number (using the `Math.sign` function).
5. We update `sumOfMagnitudes` by adding the absolute value of the current number (using the `Math.abs` function).
6. Finally, we return the product of `productOfSigns` and `sumOfMagnitudes`.

You can test this function with the examples you provided to verify that it returns the expected results. For example:
```
console.log(prodSigns([1, 2, 2, -4])); // Output: -9
console.log(prodSigns([0, 1])); // Output: 0
console.log(prodSigns([])); // Output: null
```