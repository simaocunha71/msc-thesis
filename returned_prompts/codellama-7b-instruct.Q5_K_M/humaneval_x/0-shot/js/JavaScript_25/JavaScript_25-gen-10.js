/* Return list of prime factors of given integer in the order from smallest to largest.
  Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
  Input number should be equal to the product of all factors
  >>> factorize(8)
  [2, 2, 2]
  >>> factorize(25)
  [5, 5]
  >>> factorize(70)
  [2, 5, 7]
  */
const factorize = (n) => {
  let factors = []
  let i = 2
  while (i <= n) {
    if (n % i === 0) {
      factors.push(i)
      n = n / i
    } else {
      i++
    }
  }
  return factors
}


