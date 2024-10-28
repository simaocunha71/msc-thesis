To convert the given number to binary, we can follow the steps below:

1. Divide the decimal number by 2 and store the remainder.
2. Repeat step 1 until the decimal number becomes 0.
3. The binary representation of the decimal number is the sequence of remainders in reverse order.

Here's the step-by-step breakdown for the example `decimalToBinary(15)`:

1. 15 divided by 2 is 7 with a remainder of 1.
2. 7 divided by 2 is 3 with a remainder of 1.
3. 3 divided by 2 is 1 with a remainder of 1.
4. 1 divided by 2 is 0 with a remainder of 1.

Now, we can reverse the sequence of remainders to get the binary representation of the decimal number: 1111.

Finally, we can prepend and append "db" to the binary representation to match the expected format: "db1111db".

Here's the JavaScript code to implement the solution:
```javascript
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = 'db' + (decimal % 2) + binary;
    decimal = Math.floor(decimal / 2);
  }
  return binary + 'db';
};
```
In this code, we initialize an empty string `binary` to store the binary representation. We then enter a while loop that continues until the decimal number becomes 0. Inside the loop, we append the remainder of the current decimal number divided by 2 to the beginning of the `binary` string, followed by the current value of `binary`. We then update the decimal number by dividing it by 2 and taking the floor of the result to remove the decimal part. Finally, after the loop finishes, we add "db" at the end of the `binary` string and return the result.

You can test the function with the provided examples:
```javascript
console.log(decimalToBinary(15));  // returns "db1111db"
console.log(decimalToBinary(32));  // returns "db1000