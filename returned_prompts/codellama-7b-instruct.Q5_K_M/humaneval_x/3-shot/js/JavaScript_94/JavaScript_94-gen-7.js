  var max_prime_value = 0;
  var prime_sum = 0;
  var largest_prime = [];

  for (const i of lst) {
    if (i > max_prime_value) {
      max_prime_value = i;
    }
  }

  for (const i of lst) {
    if (isPrime(i)) {
      largest_prime = i;
    }
  }

  prime_sum = largest_prime.toString().split('').map(Number).reduce((a, b) => a + b, 0);

  return prime_sum;
}



