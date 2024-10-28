  let largest = -1;

  // Divide n by 2 until n becomes odd
  while (n % 2 == 0) {
    largest = 2;
    n >>= 1;
  }

  // n must be odd at this point, thus skip the even numbers and iterate only for odd
  for (let i = 3; i * i <= n; i += 2) {
    while (n % i == 0) {
      largest = i;
      n = n / i;
    }
  }

  // This condition is to handle the case when n is a prime number
  // greater than 2
  if (n > 2) largest = n;

  return largest;
};

console.log(largestPrimeFactor(13195));
console.log(largestPrimeFactor(2048));

// Explanation:
// The function works by dividing n by 2 until n becomes odd, at which point it starts checking for factors of odd numbers starting from 3.
// It keeps track of the largest factor found so far, which is the largest prime factor of n.
// If n is still a prime number greater than 2 after the loop, it is considered as the largest prime factor.
// This method of factorization is known as trial division. It is used in this function to find the largest prime factor.
```

## 8. Check if a number is a palindrome

