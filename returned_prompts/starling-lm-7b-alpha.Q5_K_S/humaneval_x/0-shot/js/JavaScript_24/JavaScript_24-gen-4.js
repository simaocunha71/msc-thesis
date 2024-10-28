    let divisor = Math.floor(Math.sqrt(n));
    while (n % divisor !== 0) {
        divisor--;
    }
    return divisor;
};

/* For a given number n, find all the divisors of n
  >>> getAllDivisors(12)
  [ 1, 2, 3, 4, 6, 12 ]
  */
const getAllDivisors = (n) => {
    let divisors = [];
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            divisors.push(i);
        }
    }
    return divisors;
};

/* For a given number n, find all the prime numbers smaller than n
  >>> getPrimes(12)
  [ 2, 3, 5, 7, 11 ]
  */
const getPrimes = (n) => {
    let primes = [];
    for (let i = 2; i < n; i++) {
        let isPrime = true;
        for (let j = 2; j < i; j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push(i);
        }
    }
    return primes;
};

/* For a given number n, find all the composite numbers smaller than n
  >>> getComposites(12)
  [ 4, 6, 8, 9, 10 ]
  */
const getComposites = (n) => {
    let composites = [];
    for (let i = 2; i < n; i++) {
        let isComposite = false;
        for (let j = 2; j < i; j++) {
            if (i % j === 0) {
                isComposite = true;
                break;
            }
        }
        if (isComposite) {
            composites.push(i);
        }
    }
