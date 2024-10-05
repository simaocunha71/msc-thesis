  var primes = [];
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      primes.push(lst[i]);
    }
  }
  primes.sort((a, b) => b - a);
  var largestPrime = primes[0];
  var sumOfDigits = 0;
  while (largestPrime > 0) {
    sumOfDigits += largestPrime % 10;
    largestPrime = Math.floor(largestPrime / 10);
  }
  return sumOfDigits;
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}