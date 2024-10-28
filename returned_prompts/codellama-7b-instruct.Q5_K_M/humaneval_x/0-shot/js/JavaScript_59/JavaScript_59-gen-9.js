/*Return the largest prime factor of n. Assume n > 1 and is not a prime.
  >>> largestPrimeFactor(13195)
  29
  >>> largestPrimeFactor(2048)
  2
  */
const largestPrimeFactor = (n) => {
  let factors = []
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      factors.push(i)
      n = n / i
      if (n === 1) {
        return factors[factors.length - 1]
      }
    }
  }
}

