/*Return true if a given number is prime, and false otherwise.
  >>> isPrime(6)
  false
  >>> isPrime(101)
  true
  >>> isPrime(11)
  true
  >>> isPrime(13441)
  true
  >>> isPrime(61)
  true
  >>> isPrime(4)
  false
  >>> isPrime(1)
  false
  */
const isPrime = (n) => n === 2 || n === 3 || n === 5 || n === 7 || n === 11 || n === 13 || n === 17 || n === 19 || n === 23 || n === 29 || n === 31 || n === 37 || n === 41 || n === 43 || n === 47 || n === 53 || n === 59 || n === 61 || n === 67 || n === 71 || n === 73 || n === 79 || n === 83 || n === 89 || n === 97

B:
/*Return true if a given number is prime, and false otherwise.
  >>> isPrime(6)
  false
  >>> isPrime(101)
  true
  >>> isPrime(11)
  true
  >>> isPrime(13441)
  true
  >>> isPrime(61)
  true
  >>> isPrime(4)
  false
  >>> isPrime(1)
  false
  */
const isPrime = (n) => {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false
  }
  return n > 1
}

C:
/*Return true if a given number is prime, and false otherwise.
  >>> isPrime(6)
  false
  >>> isPrime(101)
  true
  >>> isPrime(11)
  true
  >>> isPrime(13441)
  true
  >>>