To solve this problem, you can follow these steps:

1. Initialize a variable `sum` to 0 to store the sum of squared numbers.
2. Iterate through each element in the list `lst`.
3. Round each element to the upper integer using `Math.ceil()`. This will ensure that all decimal parts are rounded up to the nearest whole number.
4. Square each rounded number by multiplying it by itself.
5. Add the squared number to the `sum` variable.
6. After iterating through all the elements in the list, return the final value of `sum`.

Here's an example implementation of the `sumSquares` function:

```javascript
const sumSquares = (lst) => {
  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    let rounded = Math.ceil(lst[i]);
    sum += Math.pow(rounded, 2);
  }

  return sum;
};
```

You can test the function with different inputs to verify its correctness.

For example, calling `sumSquares([1, 2, 3])` should return 14, as the squared numbers are 1, 4, and 9, and their sum is 14.

Similarly, calling `sumSquares([1, 4, 9])` should return 98, as the squared numbers are 1, 16, and 81, and their sum is 98.

Feel free to modify the code as needed to suit your specific requirements.

*/

/*
  You are given a list of numbers.
  You need to return the sum of squared numbers in the given list,
  round each element in the list to the upper int(Ceiling) first.
  Examples:
  For lst = [1,2,3] the output should be 14
  For lst = [1,4,9] the output should be 98
  For lst = [1,3,5,7] the output should be 84
  For lst = [1.4,4.2,0] the output should be