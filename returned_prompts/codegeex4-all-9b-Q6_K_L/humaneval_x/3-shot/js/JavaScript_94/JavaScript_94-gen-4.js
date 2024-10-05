  let largestPrime = Math.max(...lst.filter(isPrime));
  return sumDigits(largestPrime);

  function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i < n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  function sumDigits(n) {
    let sum = 0;
    while (n) {
      sum += n % 10;
      n = Math.floor(n / 10);
    }
    return sum;
  }
}

