You can solve this problem by checking if the number is divisible by 2 and if it is greater than or equal to 8. Here's how you can do it in JavaScript:

```javascript
const isEqualToSumEven = (n) => {
  return n % 2 === 0 && n >= 8;
}
```

The `n % 2 === 0` checks if the number is even, and `n >= 8` checks if the number is greater than or equal to 8. If both conditions are met, the function will return `true`, otherwise it will return `false`.