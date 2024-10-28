You can solve this problem by converting the number to a string, then iterating over each digit. If the digit is odd, multiply it to the product. If all digits are even, return 0.

Here is the solution:

```javascript
const digits = (n) => {
  const digits = Array.from(String(n), Number);
  let product = 1;
  for (let i = 0; i < digits.length; i++) {
    if (digits[i] % 2 !== 0) {
      product *= digits[i];
    } else if (i === digits.length - 1) {
      return 0;
    }
  }
  return product;
};
```

This solution first converts the number to an array of digits using `Array.from(String(n), Number)`. Then, it initializes the product to 1 and iterates over each digit. If the digit is odd, it multiplies it to the product. If the digit is even, it checks if it is the last digit. If it is, it returns 0. If it is not, it continues to the next digit. Finally, it returns the product.