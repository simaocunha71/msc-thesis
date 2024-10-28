```javascript
const skjkasdkd = (lst) => {
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) if (n % i === 0) return false;
    return true;
  };

  let maxPrime = 0;
  for (let num of lst) {
    if (isPrime(num) && num > maxPrime) {
      maxPrime = num;
    }
  }

  return maxPrime.toString().split("").reduce((acc, curr) => acc + parseInt(curr), 0);
};
```
Explanation:
This function first defines a helper function `isPrime` that checks if a number is prime. Then, it iterates over the input list and finds the largest prime number. Finally, it converts the prime number to a string, splits it into individual digits, and sums up the digits using the `reduce` method.

Note: The `isPrime` function uses a simple trial division method to check if a number is prime. This method is not the most efficient, but it is sufficient for this problem. For larger numbers, a more advanced primality test may be necessary. 