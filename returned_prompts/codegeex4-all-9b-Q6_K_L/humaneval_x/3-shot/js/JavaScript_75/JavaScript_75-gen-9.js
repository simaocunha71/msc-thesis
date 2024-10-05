  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) return false;
    }
    return true;
  }

  var count = 0;
  for (let i = 2; i <= a; i++) {
    if (isPrime(i) && a % i == 0) {
      count += 1;
      a = a / i;
      i = 1;
    }
  }

  return count == 3;
}



