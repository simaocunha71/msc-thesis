You can solve this problem using a simple mathematical approach. A number can be written as the sum of exactly 4 positive even numbers if and only if the number is divisible by 4. This is because the sum of four even numbers will always be an even number, and if the number is divisible by 4, it can be written as the sum of four even numbers.
Here is the solution:
```javascript
const isEqualToSumEven = (n) => {
  return n % 4 === 0;
};
```
This function will return true if the given number is divisible by 4, and false otherwise.