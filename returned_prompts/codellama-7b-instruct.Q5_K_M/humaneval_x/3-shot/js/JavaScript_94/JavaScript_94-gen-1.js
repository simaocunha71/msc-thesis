  var max_prime = 0;
  var sum = 0;

  for (const x of lst) {
    if (x > max_prime) {
      max_prime = x;
    }
  }

  while (max_prime > 0) {
    sum += max_prime % 10;
    max_prime /= 10;
  }

  return sum;
}



