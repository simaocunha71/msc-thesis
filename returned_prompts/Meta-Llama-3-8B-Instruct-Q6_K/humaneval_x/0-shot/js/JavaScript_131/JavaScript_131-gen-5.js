Here is the solution for the problem:

```javascript
const digits = (n) => {
  let product = 1;
  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
    }
    n = Math.floor(n / 10);
  }
  return product;
};
```

This function works by taking the remainder of the input number `n` when divided by 10, which gives the last digit of `n`. It then checks if this digit is odd by using the modulus operator `%`. If the digit is odd, it multiplies the product by the digit. It then removes the last digit from `n` by doing integer division by 10. This process is repeated until there are no more digits left in `n`. The final product is then returned. If all the digits in `n` are even, the product will be 1, so the function returns 0.