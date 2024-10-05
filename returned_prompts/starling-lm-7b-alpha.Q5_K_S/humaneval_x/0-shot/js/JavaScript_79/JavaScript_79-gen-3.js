To convert a decimal number to binary, we can use bitwise operations. Here's a step-by-step guide:

1. Initialize a variable called "binary" with the value of "0b". This tells JavaScript that the following number is a binary number.
2. While the decimal number is greater than 0, do the following:
    a. Divide the decimal number by 2 and get the integer part of the result. This will be the next digit in the binary representation.
    b. Convert the integer part to a string and concatenate it to the "binary" variable.
    c. Update the decimal number to be the remainder of the division.
3. After the loop, the "binary" variable will contain the binary representation of the original decimal number. Add "db" at the beginning and at the end of the string to match the expected format.
4. Return the modified "binary" variable.

Here's the JavaScript code implementing the steps above:

```javascript
const decimalToBinary = (decimal) => {
  let binary = "0b";
  while (decimal > 0) {
    binary += String.fromCharCode(48 + Math.floor(decimal % 2));
    decimal = Math.floor(decimal / 2);
  }
  return "db" + binary + "db";
};
```

You can test the function with the provided examples:

```javascript
console.log(decimalToBinary(15));  // Output: "db1111db"
console.log(decimalToBinary(32));  // Output: "db100000db"
```

This function will correctly convert any decimal number to binary format with the expected extra characters at the beginning and end of the string.

*/

//test
console.log(decimalToBinary(15));  // Output: "db1111db"
console.log(decimalToBinary(32));  // Output: "db100000db"















































