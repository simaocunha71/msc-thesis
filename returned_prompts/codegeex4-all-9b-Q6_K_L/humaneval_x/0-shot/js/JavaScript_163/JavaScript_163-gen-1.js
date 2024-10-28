The problem statement is asking to return the even digits between two positive integers `a` and `b` in ascending order.

Here are the steps to solve this problem:

1. Create a helper function `isEvenDigit(digit)` to check if a digit is even.
2. Use a loop to iterate through the range of numbers from `a` to `b`.
3. For each number, convert it to a string and check each digit if it is even.
4. If a digit is even, add it to a result array.
5. Return the result array.

Here's the JavaScript code for the solution:

```javascript
const generateIntegers = (a, b) => {
  const isEvenDigit = (digit) => digit % 2 === 0;

  let result = [];

  for (let i = a; i <= b; i++) {
    const digits = i.toString().split('').map(Number);
    for (let digit of digits) {
      if (isEvenDigit(digit)) {
        result.push(digit);
      }
    }
  }

  return result;
}
```

The time complexity of this solution is O(n * m), where n is the number of integers between `a` and `b`, and m is the average number of digits in each number.