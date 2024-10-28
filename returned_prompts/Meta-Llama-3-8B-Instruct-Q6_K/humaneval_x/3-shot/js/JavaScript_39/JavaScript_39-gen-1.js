  let a = 0, b = 1, count = 0;
  while (true) {
    let temp = a + b;
    a = b;
    b = temp;
    if (isPrime(temp)) {
      count++;
      if (count == n) {
        return temp;
      }
    }
  }
}

function isPrime(num) {
  if (num < 2) {
    return false;
  }
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}