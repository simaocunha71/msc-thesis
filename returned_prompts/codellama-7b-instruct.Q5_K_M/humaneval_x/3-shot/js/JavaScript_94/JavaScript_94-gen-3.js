  var largest_prime = 0;
  var largest_prime_sum = 0;
  var largest_prime_index = 0;

  for (var i = 0; i < lst.length; i++) {
    var prime = true;
    for (var j = 2; j < lst[i] / 2; j++) {
      if (lst[i] % j == 0) {
        prime = false;
      }
    }
    if (prime && lst[i] > largest_prime) {
      largest_prime = lst[i];
      largest_prime_sum = 0;
      for (var k = 0; k < largest_prime; k++) {
        largest_prime_sum += (largest_prime % 10);
        largest_prime /= 10;
      }
    }
  }
  return largest_prime_sum;
}



