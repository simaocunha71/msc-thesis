  let a = 0;
  let b = 1;
  let count = 1;

  while (true) {
    let temp = a;
    a = b;
    b = temp + b;
    if (isPrime(b)) {
      if (count == n) {
        return b;
      }
      count++;
    }
  }
}

function isPrime(num) {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}