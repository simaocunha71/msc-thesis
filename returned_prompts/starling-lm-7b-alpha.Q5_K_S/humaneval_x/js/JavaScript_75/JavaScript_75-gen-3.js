  const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  const max = Math.floor(Math.sqrt(a));

  for (let i = 0; i < primes.length; i++) {
    if (primes[i] > max) {
      return false;
    }

    if (a % primes[i] == 0) {
      return false;
    }
  }

  return true;
}



