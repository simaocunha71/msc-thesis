The problem can be solved by getting the last digit of each number and multiplying them together. Here is the JavaScript function that does that:

```javascript
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
}
```

This function works by using the modulus operator (`%`) to get the last digit of each number. The modulus operator returns the remainder of the division of the number before it by the number after it. So `a % 10` gives the last digit of `a`, and `b % 10` gives the last digit of `b`. Then the function multiplies these two digits together and returns the result. 

This function works for both positive and negative numbers, because the modulus operator returns the same value for positive and negative numbers. For example, `-15 % 10` is the same as `15 % 10`, which is `5`. 

This function also works for numbers with more than one digit, because the modulus operator returns the last digit of the number. For example, `2020 % 10` is `0`, and `-15 % 10` is `5`. 

So this function will correctly multiply the unit digits of two numbers, regardless of whether they are positive, negative, or have more than one digit. 