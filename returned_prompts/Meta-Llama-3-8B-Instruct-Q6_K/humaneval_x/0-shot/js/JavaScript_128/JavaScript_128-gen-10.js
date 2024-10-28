Here is a JavaScript solution for the problem:
```javascript
const prodSigns = (arr) => {
  if (arr.length === 0) return null;

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
Here's an explanation of the solution:

1. We first check if the array is empty, if so, we return null.
2. We initialize two variables: `productOfSigns` to store the product of all signs, and `sumOfMagnitudes` to store the sum of magnitudes of all numbers.
3. We iterate through the array using a `for...of` loop. For each number, we check if it's 0, if so, we return 0 because 0 multiplied by any number is 0.
4. We update `productOfSigns` by multiplying it with the sign of the current number using `Math.sign()`.
5. We update `sumOfMagnitudes` by adding the absolute value of the current number using `Math.abs()`.
6. Finally, we return the product of `productOfSigns` and `sumOfMagnitudes`.

This solution has a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1) because we only use a constant amount of space to store the intermediate results.