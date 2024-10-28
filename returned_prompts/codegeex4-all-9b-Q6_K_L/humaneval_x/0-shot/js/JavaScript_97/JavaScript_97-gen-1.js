You can use the modulo operator (%) to get the unit digit of each number and then multiply those two results together. Here's how you could do it:

```javascript
const multiply = (a, b) => {
  const unitDigitA = a % 10;
  const unitDigitB = b % 10;
  return unitDigitA * unitDigitB;
};
```

This code works by using the modulo operator (%) to get the remainder of `a` divided by 10 and `b` divided by 10. This remainder is the unit digit of `a` and `b`, respectively. Then, it returns the product of these two unit digits.

For example, if `a` is 148 and `b` is 412, `a % 10` would be 8 and `b % 10` would be 2, so the function would return 8 * 2 = 16.