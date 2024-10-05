  var largest_prime = 0;
  var largest_prime_sum = 0;

  for (let i = 0; i < lst.length; i++) {
    var current_prime = lst[i];
    var current_prime_sum = 0;

    for (let j = 0; j < current_prime; j++) {
      if (current_prime % j == 0) {
        current_prime_sum += j;
      }
    }

    if (current_prime_sum > largest_prime_sum) {
      largest_prime_sum = current_prime_sum;
      largest_prime = current_prime;
    }
  }

  return largest_prime_sum;
}



