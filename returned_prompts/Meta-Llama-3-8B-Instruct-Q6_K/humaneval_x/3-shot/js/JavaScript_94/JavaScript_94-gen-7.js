  let maxPrime = 0;
  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > maxPrime) {
        maxPrime = lst[i];
      }
    }
  }

  while (maxPrime > 0) {
    sum += maxPrime % 10;
    maxPrime = Math.floor(maxPrime / 10);
  }

  return sum;
}

const isPrime = (n) => {
  if (n <= 1) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;

  let squareRoot = Math.sqrt(n);
  for (let i = 3; i <= squareRoot; i += 2) {
    if (n % i == 0) return false;
  }

  return true;
}