You can solve this problem using the following approach:

1. Convert the integer to a string.
2. Iterate through the string and check if each character is an odd digit.
3. If a character is an odd digit, convert it back to an integer and multiply it to the product.
4. Return the product.

Here is the implementation in JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  let isAllEven = true;
  
  for (let i = 0; i < n.toString().length; i++) {
    let digit = parseInt(n.toString()[i]);
    
    if (digit % 2 !== 0) {
      product *= digit;
      isAllEven = false;
    }
  }
  
  return isAllEven ? 0 : product;
}
```

This solution works by converting the integer to a string and then iterating through each character. If a character is an odd digit, it is multiplied to the product. If all digits are even, the function returns 0.