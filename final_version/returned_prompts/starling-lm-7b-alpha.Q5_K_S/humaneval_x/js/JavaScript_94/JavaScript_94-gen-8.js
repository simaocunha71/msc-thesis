  const maxPrime = (num) => {
    let prime = 2;
    while (prime * prime <= num) {
      if (num % prime === 0) {
        return prime;
      }
      prime += 1;
    }
    return num;
  };

  const sumDigits = (num) => {
    return num.toString().split('').reduce((s, c) => s + +c, 0);
  };

  const largestPrime = lst.reduce((prev, curr) => maxPrime(prev) < maxPrime(curr) ? curr : prev);

  return sumDigits(largestPrime);
};



