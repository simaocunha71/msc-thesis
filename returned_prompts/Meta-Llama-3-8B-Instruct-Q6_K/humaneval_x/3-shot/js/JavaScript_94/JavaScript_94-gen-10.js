  let max_prime = 0;
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      if (lst[i] > max_prime) {
        max_prime = lst[i];
      }
    }
  }
  if (max_prime > 0) {
    sum = sumDigits(max_prime);
  }
  return sum;
}

function isPrime(n) {
  if (n <= 1) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  let max_divisor = Math.floor(Math.sqrt(n));
  for (let i = 3; i <= max_divisor; i += 2) {
    if (n % i == 0) return false;
  }
  return true;
}

function sumDigits(n) {
  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
}
}
}:



