  if  (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

const isPrime = (n) => {
  if  (n < 2) {
    return false;
  }
  for  (let i = 2; i < n; i++) {
    if  (n % i === 0) {
      return false;
    }
  }
  return true;
}


