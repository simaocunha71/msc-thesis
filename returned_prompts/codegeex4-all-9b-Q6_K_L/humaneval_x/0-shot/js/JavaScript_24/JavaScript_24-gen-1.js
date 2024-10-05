To find the largest number that divides `n` evenly and is smaller than `n`, you can start by checking from the largest possible divisor smaller than `n`, which is `n - 1`, and then decrement and check each number until you find a divisor of `n`. Here's how you can implement this in JavaScript:

```javascript
const largestDivisor = (n) => {
  // Start from the largest possible divisor smaller than n
  for (let i = n - 1; i > 0; i--) {
    // Check if i is a divisor of n
    if (n % i === 0) {
      return i; // Return i if it is a divisor
    }
  }
  return n; // If no divisor is found, n itself is a divisor
};

// Example usage:
console.log(largestDivisor(15)); // Output: 5
```

This function iterates from `n - 1` down to `1`, checking if each number is a divisor of `n` by using the modulo operator (`%`). If a divisor is found, the function returns it immediately. If no divisor is found, it returns `n`, as `n` itself is a divisor of `n`.