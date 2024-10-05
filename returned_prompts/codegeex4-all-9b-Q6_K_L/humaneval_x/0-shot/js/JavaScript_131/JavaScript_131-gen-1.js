Here is the solution in JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  let isEven = true;
  
  while (n > 0) {
    let digit = n % 10;
    if (digit % 2 !== 0) {
      product *= digit;
      isEven = false;
    }
    n = Math.floor(n / 10);
  }
  
  return isEven ? 0 : product;
}
```
This solution works by iterating through the digits of the number. If a digit is odd, it multiplies the current product by that digit and sets the `isEven` flag to false. If all digits are even, it returns 0. Otherwise, it returns the product.