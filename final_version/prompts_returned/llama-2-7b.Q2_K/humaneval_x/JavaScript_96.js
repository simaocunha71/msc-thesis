/*Implement a function that takes an non-negative integer and returns an array of the first n
  integers that are prime numbers and less than n.
  for example:
  countUpTo(5) => [2,3]
  countUpTo(11) => [2,3,5,7]
  countUpTo(0) => []
  countUpTo(20) => [2,3,5,7,11,13,17,19]
  countUpTo(1) => []
  countUpTo(18) => [2,3,5,7,11,13,17]
  */
const countUpTo = (n) => {
  const firstPrime = n > 0 ? primeChecker[primeChecker.length - 1] : [],
        arrayOfPriimes = [];
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      arrayOfPriimes.push(i);
    }
  }
  return arrayOfPriimes;
};

function isPrime(num) {
  // Factorial of a number.
  const nFact = factorial(num),
        nCube = cubefactor(nFact);

  if (nCube > Math.sqrt(Math.max(1, num))) return false;
  return true;
}

function primeChecker() {
  let arrayOfPrimes[] = []; // Create an empty array for storing the primes
  for (let i = 0; i <= n; i++) { // Loop through each iteration of the value of 'i' from 2 to n. 2 is needed here as primeChecker[primeChecker.length -1] only stores one element, where each element is a number larger than 1.
    if (isPrime(i)) arrayOfPrimes.push(i); // Each iteration in the loop is pushing 'i' to arrayOfPrimes to store all prime numbers of the input range until it reaches n.
  }
}