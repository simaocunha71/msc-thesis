  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

function isPrime(num) {
  if (num <= 1) return false;
  if (num == 2) return true;
  if (num % 2 == 0) return false;

  var sqrt = Math.sqrt(num);

  for (var i = 3; i <= sqrt; i += 2) {
    if (num % i == 0) return false;
  }

  return true;
}