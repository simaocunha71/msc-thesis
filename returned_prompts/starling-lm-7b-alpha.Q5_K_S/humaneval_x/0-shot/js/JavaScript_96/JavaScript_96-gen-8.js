  let primes = [];
  let isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
  }
  return primes;
};

/*
Implement a function that takes an array of non-negative numbers and returns an array of
the first n numbers that are prime numbers. The function should return an array of
the first n prime numbers less than the largest number in the input array.
  for example:
  findPrimes(countUpTo(5)) => [2,3]
  findPrimes(countUpTo(11)) => [2,3,5,7]
  findPrimes([0,10]) => [2,3,5,7]
  findPrimes([0,20]) => [2,3,5,7,11,13,17,19]
  findPrimes([1,20]) => [2,3,5,7,11,13,17,19]
  findPrimes([0,1]) => []
  findPrimes([1,18]) => [2,3,5,7,11,13,17]
  findPrimes([2,20]) => [2,3,5,7,11,13,17,19]
  */

const findPrimes = (nums) => {
  let max = Math.max(...nums);
  return countUpTo(max);
}

module.exports = {
  countUpTo,
  findPrimes
}

































































