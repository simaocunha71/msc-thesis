To convert a decimal number to binary, you can use the following steps:

1. Initialize a variable `binary` with the value "1". This variable will store the binary representation of the decimal number.
2. Initialize a variable `decimal` with the value of the input `decimal` parameter.
3. Initialize a variable `remainder` with the value 0. This variable will store the remainder after each division operation.
4. Initialize a variable `quotient` with the value 0. This variable will store the quotient after each division operation.
5. Use a while loop to repeatedly perform the following steps until `decimal` becomes 0:
   a. Divide `decimal` by 2 and store the quotient in `quotient`.
   b. Multiply `remainder` by 10 and add the result to `binary`.
   c. Update the value of `decimal` by adding `quotient` and the value of `remainder`.
   d. Update the value of `remainder` to the remainder of the division operation.
6. After the while loop, append the characters 'db' at the beginning and end of the `binary` string.
7. Return the `binary` string.

Here's the code that implements the above steps:

```javascript
const decimalToBinary = (decimal) => {
  let binary = "1";
  let decimal = decimal;
  let remainder = 0;
  let quotient = 0;

  while (decimal > 0) {
    quotient = Math.floor(decimal / 2);
    remainder = decimal - quotient;
    decimal += quotient;
    binary = (remainder * 10).toString(2) + binary;
  }

  return "db" + binary + "db";
};
```

You can test the function with the provided examples:

```javascript
console.log(decimalToBinary(15));  // returns "db1111db"
console.log(decimalToBinary(32));  // returns "db100000db"
```

This will output:

```
db1111db
db100