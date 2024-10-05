  let largest = 0;
  for (let i = 2; i <= n; i++) {
    if (n % i == 0 && isPrime(i)) {
      largest = i;
    }
  }
  return largest;
}

const isPrime = (n) => {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}



