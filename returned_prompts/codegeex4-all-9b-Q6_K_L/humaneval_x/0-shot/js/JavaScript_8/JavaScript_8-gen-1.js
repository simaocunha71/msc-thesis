Here is the solution in JavaScript:

```javascript
const sumProduct = (numbers) => {
  let sum = 0;
  let product = 1;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }

  return (sum, product);
}
```
This function takes an array of integers as input, calculates the sum and product of the integers, and returns them as a tuple. If the array is empty, the sum is 0 and the product is 1.