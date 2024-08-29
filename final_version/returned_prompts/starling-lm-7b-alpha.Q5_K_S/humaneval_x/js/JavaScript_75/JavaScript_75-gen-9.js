  const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  let n = a;
  let result = true;

  for (let i = 0; i < primes.length; i++) {
    if (primes[i] > n) {
      break;
    }

    while (n % primes[i] == 0) {
      n = n / primes[i];
    }

    if (n == 1) {
      break;
    } else {
      result = false;
    }
  }
  return result;
}



