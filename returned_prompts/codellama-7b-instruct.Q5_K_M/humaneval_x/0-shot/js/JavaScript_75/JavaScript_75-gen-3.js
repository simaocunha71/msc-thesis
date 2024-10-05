const isPrime = (n) => {
  if (n === 1 || n === 0) return false;
  for (let i = 2; i < n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
const getPrimeFactors = (a) => {
  const factors = [];
  for (let i = 0; i < a; i++) {
    if (isPrime(i)) factors.push(i);
  }
  return factors;
};

const isMultiplyPrime = (a) => {
  const factors = getPrimeFactors(a);
  for (let i = 0; i < factors.length; i++) {
    if (a % factors[i] !== 0) return false;
  }
  return true;
};
