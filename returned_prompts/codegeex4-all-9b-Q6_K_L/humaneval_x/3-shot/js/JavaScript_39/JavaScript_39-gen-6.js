  var count = 0;
  var current = 2;
  var next = 3;
  while (count < n) {
    if (isPrime(current)) {
      count += 1;
      if (count == n) {
        return current;
      }
    }
    if (isPrime(next)) {
      count += 1;
      if (count == n) {
        return next;
      }
    }
    var temp = current;
    current = next;
    next = next + temp;
  }
}

const isPrime = (number) => {
  if (number == 2) {
    return true;
  }
  for (let i = 2; i < number; i++) {
    if (number % i == 0) {
      return false;
    }
  }
  return true;
}