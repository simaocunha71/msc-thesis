The solution is to check the factors of n starting from the largest possible factor (which is n itself) and stop when we find a prime factor. If n is a prime number, then its only prime factor is itself. If n is not a prime number, then its largest prime factor must be less than or equal to n/2 (if n/2 is not prime, then the largest prime factor must be less than n/2).

Here is the solution:
```javascript
const largestPrimeFactor = (n) => {
  let maxFactor = Math.floor(n/2);
  for (let i = maxFactor; i > 1; i--) {
    if (n % i === 0 && isPrime(i)) {
      return i;
    }
  }
  return n;
}

// Function to check if a number is prime
const isPrime = (num) => {
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
    if (num % i === 0) return false;
  return num > 1;
}
```