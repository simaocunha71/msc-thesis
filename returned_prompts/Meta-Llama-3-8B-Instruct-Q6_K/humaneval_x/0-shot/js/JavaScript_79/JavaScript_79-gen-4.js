Here is the JavaScript solution for the problem:

```javascript
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = (decimal % 2).toString() + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
};
```

In this solution, we use a while loop to convert the decimal number to binary. In each iteration, we take the remainder of the decimal number when divided by 2 as the next binary digit. We add this digit to the beginning of the binary string. Then, we update the decimal number by performing integer division by 2. The process continues until the decimal number becomes 0. Finally, we add the extra 'db' characters to the beginning and end of the binary string and return the result.