/*Return the largest prime factor of n. Assume n > 1 and is not a prime.
  >>> largestPrimeFactor(13195)
  29
  >>> largestPrimeFactor(2048)
  2
  */
const largestPrimeFactor = (n) => {
  var primeFactors = [];
  var i = 2;
  while (n > 1) {
    if (n % i === 0) {
      primeFactors.push(i);
      n /= i;
    } else {
      i++;
    }
  }
  return primeFactors[primeFactors.length - 1];
}

