    let i = 2;
    while (n % i !== 0) {
        i++;
    }
    return i;
};


/*
Return all the prime factors of n. Assume n > 1 and is not a prime.
  >>> primeFactors(2048)
  [ 2, 2, 2, 2, 2 ]
  >>> primeFactors(13195)
  [ 5, 7, 11, 29 ]

*/
const primeFactors = (n) => {
    const result = [];

    while (n % 2 === 0) {
        result.push(2);
        n /= 2;
    }

    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        while (n % i === 0) {
            result.push(i);
            n /= i;
        }
    }

    if (n > 2) result.push(n);
    return result;
};

/*
Return the smallest prime number that is greater than n.
  >>> smallestPrimeGreaterThan(3)
  5
  >>> smallestPrimeGreaterThan(20)
  23

*/
const smallestPrimeGreaterThan = (n) => {
    let candidate = n + 1;
    while (!isPrime(candidate)) {
        candidate++;
    }
    return candidate;
};

/*
Return whether n is prime. Assume n > 1.
  >>> isPrime(7)
  True
  >>> isPrime(10)
  False

*/
const isPrime = (n) => {
    if (n <= 1) return false;
    if (n <= 3) return true;

    if (n % 2 === 0 || n % 3 === 0) return false;

    for (let i = 5; i * i <= n; i += 6) {
        if (n % i === 0 || n % (i + 2) === 0) return false;
    }

    return true;