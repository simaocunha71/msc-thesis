To find the largest number that divides n evenly, smaller than n, you can use a for loop to start from n/2 and go down to 1. In each iteration, check if n is divisible evenly by the current number. If it is, return the current number as the largest divisor. If not, continue to the next iteration. If no divisor is found, return -1 to indicate that no divisor exists for the given number. Here's an example implementation in JavaScript:

```javascript
const largestDivisor = (n) => {
  for (let i = Math.floor(n / 2); i >= 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return -1;
};

console.log(largestDivisor(15));  // Output: 5
```

In this example, the function `largestDivisor` takes a number `n` as input. It starts the loop from `n/2` because any number greater than `n/2` cannot be a divisor of `n`. The loop continues until `i` becomes 1. Inside the loop, it checks if `n` is divisible evenly by `i` using the modulo operator (`%`). If the remainder is 0, it means `i` is a divisor of `n`, so it is returned as the largest divisor. If no divisor is found, the function returns -1.

For the given input `15`, the function will return `5` as the largest number that divides `15` evenly and is smaller than `15`.

Note that this implementation assumes that the input `n` is a positive integer. If you need to handle other types of inputs or edge cases, additional validation and error handling may be required.

I hope this helps! Let me know if you have any more questions.

Best regards,
Eric
*/

```javascript
const largestDivisor = (n) => {
  for (let i = Math.floor(n / 2); i >= 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return -1