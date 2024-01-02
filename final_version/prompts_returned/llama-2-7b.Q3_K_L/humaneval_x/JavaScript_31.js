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
  if (!Number.isInteger(n)) return false;
  if ((n - 1) % n === 0 && n > 3) return true;
  
  let sqrtOfN = Math.sqrt(n);
  
  for (let i = 2; i < sqrtOfN; i++) {
    if (i * i % n !== 0 || n - (i * i) === 1) return false;
  }
  return true;
}
console.log(isPrime(6)); // false
console.log(isPrime(101)); // true
console.log(isPrime(11)); // true
console.log(isPrime(13441)); // true
console.log(isPrime(61)); // true
console.log(isPrime(4)); // false
console.log(isPrime(1)); // false