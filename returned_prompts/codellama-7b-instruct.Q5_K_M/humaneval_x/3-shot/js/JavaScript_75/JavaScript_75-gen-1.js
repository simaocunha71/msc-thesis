  var prime_numbers = [2, 3, 5];
  var product = 0;

  if (a < 100) {
    for (let i = 0; i < prime_numbers.length; i++) {
      for (let j = 0; j < prime_numbers.length; j++) {
        if (a == (prime_numbers[i] * prime_numbers[j])) {
          return true;
        }
      }
    }
    return false;
  }
}



