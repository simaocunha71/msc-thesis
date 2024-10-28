The problem can be solved by converting the integer into a string, then iterating over each character (digit) in the string. Check if the digit is odd, if it is, multiply it with the current product. If all digits are even, return 0. Here is the solution in JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  let oddCount = 0;
  n.toString().split('').forEach(digit => {
    if (+digit % 2 !== 0) {
      product *= +digit;
      oddCount++;
    }
  });
  return oddCount > 0 ? product : 0;
};
```

In this solution, we first convert the integer into a string using `toString()`. Then we split the string into an array of characters using `split('')`. We iterate over each character in the array using `forEach()`. If the character (digit) is odd (i.e., `+digit % 2 !== 0`), we multiply the current product with the digit and increment the `oddCount`. Finally, if there are any odd digits, we return the product, otherwise we return 0.