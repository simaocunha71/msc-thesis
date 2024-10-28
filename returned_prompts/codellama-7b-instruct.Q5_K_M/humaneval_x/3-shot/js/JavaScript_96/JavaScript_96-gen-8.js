  var prime_numbers = [];

  for (var i = 0; i < n; i++) {
    var is_prime = true;
    for (var j = 2; j < i; j++) {
      if (i % j == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      prime_numbers.push(i);
    }
  }

  return prime_numbers;
}



