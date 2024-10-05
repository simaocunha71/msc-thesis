  let maxPrime = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > maxPrime) {
        maxPrime = lst[i];
      }
    }
  }
  return sumDigits(maxPrime);
}

function isPrime(n) {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function sumDigits(n) {
  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
}