You can use the following function to solve the problem:

```javascript
const digits = (n) => {
  let product = 1;
  while (n > 0) {
    const digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
};
```

This function works by repeatedly taking the remainder of the input number `n` when divided by 10 (`n % 10`) to get the last digit, and then checking if that digit is odd by using the modulus operator (`%`) with 2. If the digit is odd, it multiplies the product by that digit. It then removes the last digit from the input number by integer dividing by 10 (`Math.floor(n / 10)`). It repeats this process until there are no more digits left in the input number. If there are no odd digits in the input number, the function returns 0. Otherwise, it returns the product of the odd digits.