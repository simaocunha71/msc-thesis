  let largest_prime = 2;
  for (const num of lst) {
    if (isPrime(num) && num > largest_prime) {
      largest_prime = num;
    }
  }

  let sum_digits = 0;
  while (largest_prime > 0) {
    sum_digits += largest_prime % 10;
    largest_prime = Math.floor(largest_prime / 10);
  }

  return sum_digits;
}

const isPrime = (num) => {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}



