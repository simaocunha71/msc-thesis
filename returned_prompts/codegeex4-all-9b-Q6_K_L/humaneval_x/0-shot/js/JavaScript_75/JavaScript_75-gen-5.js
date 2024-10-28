```javascript
  const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  let count = 0;
  for (let i = 0; i < primes.length; i++) {
    while (a % primes[i] === 0) {
      a /= primes[i];
      count++;
    }
  }
  return count === 3;
};
```

This function first creates an array of prime numbers less than 100. Then it iterates through the array and checks if the given number can be divided by each prime number. If it can, it divides the given number by the prime number and increments the count. Finally, it returns true if the count is equal to 3, indicating that the given number is a multiplication of 3 prime numbers.