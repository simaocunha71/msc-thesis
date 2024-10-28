  let i = 2;
  let maxFactor = 1;

  while (i * i <= n) {
    if (n % i) {
      i++;
    } else {
      n = n / i;
      while (n % i === 0) {
        n = n / i;
      }
      maxFactor = i;
    }
  }

  if (n > 1) {
    maxFactor = n;
  }

  return maxFactor;
}
// The idea here is to start from 2 and keep dividing the number by 2 as long as it's divisible
// Then increment the divisor until we find a number that is not divisible. That will be the largest prime factor
// If the remaining number is more than 1, that means it's a prime number itself, so we return it as the largest prime factor
// The key is to understand the concept of prime factorization and how to implement it. This solution has a time complexity of O(sqrt(n))
// It's not the most efficient solution but it's simple and easy to understand. For large numbers, a more efficient solution would be needed.