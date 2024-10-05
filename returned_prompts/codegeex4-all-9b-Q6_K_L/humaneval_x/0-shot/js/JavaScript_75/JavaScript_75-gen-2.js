const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const isMultiplyPrime = (a) => {
  const primes = [];
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) primes.push(i);
  }
  let product = 1;
  for (let j = 0; j < primes.length; j++) {
    product *= primes[j];
    if (product === a) return true;
    if (product > a) break;
  }
  return false;
};

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(28)); // false