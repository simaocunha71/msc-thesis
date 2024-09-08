  let max_prime_number = 0;
  let sum_of_digits = 0;

  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
      max_prime_number = lst[i];
    }
  }

  while (max_prime_number > 0) {
    sum_of_digits += max_prime_number % 10;
    max_prime_number = Math.floor(max_prime_number / 10);
  }

  return sum_of_digits;
}



