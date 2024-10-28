  let a = 0, b = 1;
  for (let i = 0; i < n; i++) {
    let temp = a;
    a = b;
    b = temp + b;
    if (isPrime(b)) {
      return b;
    }
  }
}

const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}
}