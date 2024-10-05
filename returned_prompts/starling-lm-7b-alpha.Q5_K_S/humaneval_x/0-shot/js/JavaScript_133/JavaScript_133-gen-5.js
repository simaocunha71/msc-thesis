To solve this problem, you need to follow these steps:

1. Round each element in the list to the upper integer (ceiling).
2. Square each element in the rounded list.
3. Sum all the squared numbers.

Here's a step-by-step explanation of the solution:

Step 1: Round each element in the list to the upper integer (ceiling).
To round each element to the upper integer, you can use the `Math.ceil()` function in JavaScript. This function rounds a number up to the nearest integer. You can apply `Math.ceil()` to each element in the list using the `map()` function. This will create a new list with rounded elements.

Step 2: Square each element in the rounded list.
To square each element in the rounded list, you can use the `Math.pow()` function. This function returns the base (number) to the power of the exponent (number). In this case, the exponent will always be 2. Again, you can use the `map()` function to apply `Math.pow()` to each element in the rounded list. This will create a new list with squared elements.

Step 3: Sum all the squared numbers.
To sum all the squared numbers in the list, you can use the `reduce()` function. This function iterates over each element in the list and applies a function to reduce the list to a single value. In this case, the function will be addition. The initial value of the sum will be 0, and the function will add each squared number to the sum.

Here's an example implementation of the solution:

```javascript
const sumSquares = (lst) => {
  // Step 1: Round each element in the list to the upper integer (ceiling)
  const roundedList = lst.map(Math.ceil);

  // Step 2: Square each element in the rounded list
  const squaredList = roundedList.map(num => Math.pow(num, 2));

  // Step 3: Sum all the squared numbers
  const result = squaredList.reduce((acc, cur) => acc + cur, 0);

  return result;
};
```

You can use this `sumSquares