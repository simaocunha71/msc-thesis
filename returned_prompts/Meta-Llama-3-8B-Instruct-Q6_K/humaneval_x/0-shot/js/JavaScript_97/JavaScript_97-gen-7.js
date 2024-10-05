```
const multiply = (a, b) => {
  return (Math.abs(a) % 10) * (Math.abs(b) % 10);
};
```


Explanation:

The function takes two integers `a` and `b` as input and returns the product of their unit digits.

To get the unit digit of a number, we use the modulus operator `%` with 10. This gives us the remainder of the division of the number by 10, which is the last digit of the number.

We use `Math.abs()` to get the absolute value of the input numbers, in case one of them is negative. This is because the unit digit of a negative number is the same as the unit digit of its absolute value.

Finally, we multiply the unit digits of `a` and `b` and return the result. If either of the input numbers is negative, the product will still be correct because the unit digits are the same for positive and negative numbers.