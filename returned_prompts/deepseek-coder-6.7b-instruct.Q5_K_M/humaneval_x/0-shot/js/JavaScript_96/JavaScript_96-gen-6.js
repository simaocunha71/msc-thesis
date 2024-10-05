const countUpTo = n => {
  // An array to store the prime numbers
  const primes = [];

  // Check if a number is prime
  const isPrime = num => {
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return num > 1;
  }

  // Iterate through all numbers up to n
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) primes.push(i);
  }

  // Return the array of prime numbers
  return primes;
}

console.log(countUpTo(5)); // [2, 3]
console.log(countUpTo(11)); // [2, 3, 5, 7]
console.log(countUpTo(0)); // []
console.log(countUpTo(20)); // [2, 3, 5, 7, 11, 13, 17, 19]
console.log(countUpTo(1)); // []
console.log(countUpTo(18)); // [2, 3, 5, 7, 11, 13, 17]

// This solution assumes n >= 0
```

This solution works by creating an array of prime numbers less than n. It uses a helper function, isPrime(), to check if each number up to n is prime. If a number is prime, it is added to the primes array. Finally, the primes array is returned.

This solution assumes that n is a non-negative integer.
```

# Problem 2:

