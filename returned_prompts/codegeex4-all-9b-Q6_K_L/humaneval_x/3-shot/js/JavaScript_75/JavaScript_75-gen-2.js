  var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  var result = true;
  var i = 0;
  var count = 0;
  while (result && i < primes.length) {
    while (a % primes[i] == 0) {
      a = a / primes[i];
      count += 1;
    }
    if (count == 0) {
      result = false;
    }
    count = 0;
    i += 1;
  }
  return result;
}



