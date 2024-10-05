```javascript
const sumProduct = (numbers) => {
  if (numbers.length === 0) {
    return [0, 1];
  }
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
    product *= numbers[i];
  }
  return [sum, product];
};
```


Explanation:
The function `sumProduct` takes an array of numbers as an argument and returns a tuple containing the sum and product of all the numbers in the array.

In the case of an empty array, the function returns a tuple with sum equal to 0 and product equal to 1.

In the case of a non-empty array, the function iterates over the array, summing up all the numbers and multiplying them together. The sum and product are returned as a tuple.

The function is tested with the examples provided in the problem description. For an empty array, the function returns (0, 1) as expected. For an array with numbers [1, 2, 3, 4], the function returns (10, 24) as expected.