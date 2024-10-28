Here is a JavaScript solution for the problem:

```javascript
const decimalToBinary = (decimal) => {
  let binary = decimal.toString(2);
  return "db" + binary.padStart(8, '0') + "db";
};
```

Explanation:

1. We convert the decimal number to a binary string using the `toString(2)` method.
2. We use the `padStart` method to add leading zeros to the binary string, ensuring it has a length of 8 characters (since we're adding 'db' at the beginning and end, the total length will be 10).
3. We concatenate the 'db' strings with the binary string to form the final result.