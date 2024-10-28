You can solve this problem by converting the integer to a string and then iterating over each character. If the character is an odd digit, you multiply it to the product. If the character is an even digit, you return 0. Here is a solution in JavaScript:

```javascript
const digits = (n) => {
  let product = 1;
  let isAllEven = true;
  const str = n.toString();
  for (let i = 0; i < str.length; i++) {
    const digit = parseInt(str[i]);
    if (digit % 2 === 0) {
      return 0;
    } else {
      product *= digit;
      isAllEven = false;
    }
  }
  return isAllEven ? 0 : product;
};
```

This function first initializes the product to 1 and a boolean variable `isAllEven` to true. Then it converts the integer `n` to a string and iterates over each character. If the character is an even digit, it returns 0. Otherwise, it multiplies the character to the product and updates `isAllEven` to false. Finally, it returns the product if there is at least one odd digit, otherwise it returns 0.