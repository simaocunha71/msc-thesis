  let a = 0, b = 1, count = 0;
  while (true) {
    let temp = a;
    a = b;
    b = temp + b;
    if (isPrime(b)) {
      count++;
      if (count == n) {
        return b;
      }
    }
  }
}

function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}