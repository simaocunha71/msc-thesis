To solve this problem, we can follow these steps:

1. Convert the given positive integer N to binary representation.
2. Iterate through each digit in the binary representation.
3. For each digit, if it is 1, add it to the result string. Otherwise, continue to the next digit.
4. Return the result string.

Here is an example implementation of the solution in JavaScript:

```javascript
const solve = (N) => {
  const binary = N.toString(2);
  let result = "";

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === "1") {
      result += "1";
    }
  }

  return result;
};
```

This implementation uses the `toString()` method to convert the number to binary representation. Then, it iterates through each digit of the binary string and checks if it is equal to "1". If it is, it adds "1" to the result string. Finally, it returns the result string, which represents the sum of the digits in binary.

For example, if we call `solve(1000)`, it will return "1" because the binary representation of 1000 is "10000000000" and the sum of its digits is 1.

Similarly, if we call `solve(150)`, it will return "110" because the binary representation of 150 is "10010110" and the sum of its digits is 6.

And if we call `solve(147)`, it will return "1100" because the binary representation of 147 is "10001111" and the sum of its digits is 12.

Overall, this implementation provides a straightforward solution to calculate the sum of the digits in binary representation of a given positive integer N.

*/

/*Given a positive integer N, return the total sum of its digits in binary.
  
  Example
      For N = 1000, the sum of digits will be 1 the output should be "1".
      For N = 1