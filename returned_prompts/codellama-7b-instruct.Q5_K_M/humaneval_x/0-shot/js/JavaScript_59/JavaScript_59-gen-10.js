/*Return the largest prime factor of n. Assume n > 1 and is not a prime.
  >>> largestPrimeFactor(13195)
  29
  >>> largestPrimeFactor(2048)
  2
  */
const largestPrimeFactor = (n) => {
  for (let i = n; i > 1; i--) {
    if (n % i === 0 && isPrime(i)) {
      return i;
    }
  }
  return 1;
};

