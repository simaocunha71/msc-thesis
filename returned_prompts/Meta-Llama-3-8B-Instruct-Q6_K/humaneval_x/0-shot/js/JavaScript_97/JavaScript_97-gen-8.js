```
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
};
```


This solution uses the modulus operator (`%`) to get the last digit of each number (the "unit digit"). It then returns the product of these two digits. This works because the modulus operator returns the remainder of the division of the number by the divisor, and since we're using it with a divisor of 10, it effectively gives us the last digit of the number. For example, `14 % 10` would give us `4`, and `15 % 10` would give us `5`. We can then multiply these two digits together to get the product of the unit digits. This solution is simple and efficient, and it works for all valid inputs.