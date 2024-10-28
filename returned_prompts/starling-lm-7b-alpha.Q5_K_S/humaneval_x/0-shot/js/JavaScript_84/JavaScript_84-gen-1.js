In this kata, we are asked to calculate the sum of digits of a number in binary notation.

To solve this problem, we can follow these steps:

1. Convert the number into binary using the built-in `.toString(2)` method. This will convert the number into a binary string.
2. Initialize a variable `sum` to keep track of the sum of binary digits. Set it to `0`.
3. Iterate through each digit in the binary string. For each digit, check if it is equal to `'1'`. If it is, add `1` to the `sum` variable. Otherwise, add `0`.
4. After iterating through all the digits, convert the `sum` variable to a binary string using the `.toString(2)` method. This will ensure that the final result is in binary notation.
5. Return the binary representation of the sum.

Here's an example implementation of the solution in JavaScript:

```javascript
const solve = (N) => {
  const binary = N.toString(2);
  let sum = 0;

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      sum += 1;
    }
  }

  return sum.toString(2);
};
```

This implementation first converts the input number `N` into a binary string using the `.toString(2)` method. Then, it initializes a variable `sum` to `0` to keep track of the sum of binary digits. Next, it iterates through each digit in the binary string and checks if it is equal to `'1'`. If it is, it adds `1` to the `sum` variable. Otherwise, it adds `0`. Finally, it converts the `sum` variable to a binary string using the `.toString(2)` method and returns the result.

This solution will correctly calculate the sum of digits of a number in binary notation.

*/

/*
Given a positive integer N, return the total sum of its digits in binary.

Example
    For N = 1000, the sum of digits will be 1 the output should be "1".
   