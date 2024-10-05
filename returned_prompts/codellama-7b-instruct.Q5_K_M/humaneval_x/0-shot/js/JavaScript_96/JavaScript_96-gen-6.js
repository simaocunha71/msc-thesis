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
    let arr = [];
    for (let i = 2; i < n; i++) {
      if (isPrime(i)) {
        arr.push(i);
      }
    }
    return arr;
  }

  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  const countUpTo = (n) => {
    let arr = [];
    for (let i = 2; i <= n; i++) {
      arr.push(i);
    }
    return arr.filter(num => isPrime(num));
  }

  const isPrime = (num) => {
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  const countUpTo = (n) => {
    const primes = [];
    for (let i = 0; i < n; i++) {
      if (isPrime(i)) {
        primes.push(i);
      }
    }
    return primes;
  }

  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 