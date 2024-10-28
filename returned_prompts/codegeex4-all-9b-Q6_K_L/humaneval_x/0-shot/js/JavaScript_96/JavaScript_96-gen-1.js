Here is a possible solution in JavaScript:

```javascript
const countUpTo = (n) => {
  // Array to hold the prime numbers
  let primes = [];

  // Function to check if a number is prime
  const isPrime = (num) => {
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false; 
    return num > 1;
  }

  // Iterate from 2 to n-1
  for (let i = 2; i < n; i++) {
    // If the number is prime, add it to the array
    if (isPrime(i)) primes.push(i);
  }

  // Return the array of prime numbers
  return primes;
}
```

This function works by iterating from 2 to n-1, and for each number, it checks whether it is prime using the `isPrime` function. If the number is prime, it is added to the `primes` array. Finally, the `primes` array is returned.