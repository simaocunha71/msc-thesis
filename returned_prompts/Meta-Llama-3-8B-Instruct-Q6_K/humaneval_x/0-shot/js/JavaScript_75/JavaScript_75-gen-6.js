```
const isMultiplyPrime = (a) => {
  function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  let factors = [];
  for (let i = 2; i <= a; i++) {
    if (a % i === 0 && isPrime(i)) {
      factors.push(i);
    }
  }
  return factors.length === 3;
};
```


Explanation:

1. First, we define a helper function `isPrime` that checks if a given number is prime or not.
2. Then, we define the main function `isMultiplyPrime` that takes an integer `a` as input.
3. We initialize an empty array `factors` to store the prime factors of the number `a`.
4. We iterate through the numbers from 2 to `a` and check if the number is a factor of `a` and if it's prime using the `isPrime` function.
5. If the number is a factor and prime, we add it to the `factors` array.
6. Finally, we return `true` if the length of the `factors` array is 3 (i.e., `a` is the multiplication of 3 prime numbers), and `false` otherwise.