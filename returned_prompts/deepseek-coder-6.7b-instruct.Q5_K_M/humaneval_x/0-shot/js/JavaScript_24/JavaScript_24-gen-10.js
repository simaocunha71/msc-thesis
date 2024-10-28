  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15));

// This solution works by iterating from n - 1 down to 1, checking if n is divisible by the current number. 
// If it is, then that current number is the largest divisor of n, so it is returned.
// The loop ensures that the function returns the largest such number as soon as it is found.
// If no such number is found (which would only happen if n is 1), the function will return 1, as 1 is the smallest divisor of all numbers.
```

### 1.8.3. 
```JS
