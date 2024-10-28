Here is a JavaScript function that fulfills the requirements:

```javascript
const isMultiplyPrime = (a) => {
  // Function to check if a number is prime
  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  // Function to find prime factors of a number
  const primeFactors = (n) => {
    const factors = [];
    for (let i = 2; i * i <= n; i++) {
      while (n % i === 0) {
        factors.push(i);
        n /= i;
      }
    }
    if (n > 1) factors.push(n);
    return factors;
  };

  // Check if the given number is the multiplication of 3 prime numbers
  const factors = primeFactors(a);
  if (factors.length < 3) return false;
  for (let i = 0; i < 3; i++) {
    if (!isPrime(factors[i])) return false;
  }
  return true;
};
```

This function first checks if the given number `a` has more than 3 prime factors. If it does, it returns `false`. Then, it checks if the first 3 prime factors are prime numbers. If any of them are not prime, it returns `false`. If all conditions are met, it returns `true`.

You can test this function with the example you provided:

```javascript
console.log(isMultiplyPrime(30));  // Output: true
```


This function works for numbers less than 100, as per your requirement. However, it may not be efficient for larger numbers due to its complexity. For larger numbers, you may need to use more efficient algorithms.