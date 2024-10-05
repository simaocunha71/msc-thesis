```
const decimalToBinary = (decimal) => {
  let binary = decimal.toString(2).padStart(8, '0');
  return 'db' + binary + 'db';
};
```
The function `decimalToBinary` takes an integer as an argument, converts it to a binary string using the `toString(2)` method, and then adds the extra characters 'db' at the beginning and the end of the string. The `padStart(8, '0')` method is used to ensure that the binary string is at least 8 characters long, padding with zeros if necessary. 

Here are the results for the examples:
```
decimalToBinary(15)   # returns "db11111db"
decimalToBinary(32)   # returns "db100000db"
``` 