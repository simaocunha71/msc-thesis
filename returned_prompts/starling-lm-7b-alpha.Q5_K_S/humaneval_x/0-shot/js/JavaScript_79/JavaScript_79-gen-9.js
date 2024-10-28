To convert a decimal number to a binary number, you can follow these steps:
1. Initialize an empty string variable called `binary` to store the binary representation of the decimal number.
2. While the decimal number is greater than 0, do the following steps:
   a. Calculate the remainder of the decimal number divided by 2. This remainder will be the last digit of the binary number.
   b. Append the remainder (either 0 or 1) to the `binary` string.
   c. Divide the decimal number by 2, and round down to the nearest whole number. This will be the new decimal number to process.
3. After the loop, the `binary` string will contain the binary representation of the original decimal number.
4. Append "db" to the beginning and end of the `binary` string, and return the resulting string.

Here's the code implementation of the above steps:

```javascript
const decimalToBinary = (decimal) => {
  let binary = '';

  while (decimal > 0) {
    binary = (decimal % 2) + binary;
    decimal = Math.floor(decimal / 2);
  }

  return 'db' + binary + 'db';
};
```

For example, if you call `decimalToBinary(15)`, it will return "db1111db", and if you call `decimalToBinary(32)`, it will return "db100000db".

This implementation converts the decimal number to binary using the modulus operator (`%`) and integer division (`Math.floor()`). The binary digits are appended to the `binary` string in reverse order, from the least significant bit to the most significant bit. Finally, "db" is added to the beginning and end of the `binary` string to match the required format.

Note: This solution assumes that the input `decimal` is a positive integer and does not handle non-integer values or negative numbers.

*/

// Example usage:
console.log(decimalToBinary(15));    // Output: "db1111db"
console.log(decimalToBinary(32));    // Output: "db10000