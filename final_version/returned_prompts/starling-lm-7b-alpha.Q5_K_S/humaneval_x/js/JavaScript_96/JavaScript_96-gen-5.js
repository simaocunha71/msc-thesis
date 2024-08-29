  const sieve = [];

  for (let i = 0; i < n; i++) {
    sieve[i] = true;
  }

  sieve[0] = false;
  sieve[1] = false;

  for (let i = 2; i * i < n; i++) {
    if (sieve[i]) {
      for (let j = i * i; j < n; j += i) {
        sieve[j] = false;
      }
    }
  }

  let result = [];
  for (let i = 2; i < n; i++) {
    if (sieve[i]) {
      result.push(i);
    }
  }

  return result;
}



