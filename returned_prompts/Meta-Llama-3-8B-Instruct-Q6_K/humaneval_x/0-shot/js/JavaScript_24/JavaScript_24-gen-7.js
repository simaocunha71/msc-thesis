Here is the solution to the problem:

```javascript
const largestDivisor = (n) => {
  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};

// Test the function
console.log(largestDivisor(15)); // Output: 5
```

In this solution, we use a for loop to iterate from the number n down to 1. For each iteration, we check if n is divisible by the current number i using the modulus operator (%). If n is divisible by i, we return i as the largest divisor. If the loop finishes without finding a divisor, we return 1 as the largest divisor, which is 1 for any number. The function is then tested with the input 15, which returns the largest divisor 5.