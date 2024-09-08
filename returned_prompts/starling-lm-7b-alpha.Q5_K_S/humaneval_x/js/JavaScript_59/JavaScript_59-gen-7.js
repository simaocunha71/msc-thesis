  const isPrime = (number) => {
    for (let i = 2; i < number; i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return true;
  };

  let current = n;
  while (current % 2 == 0) {
    current = current / 2;
  }

  while (current > 2) {
    if (isPrime(current)) {
      return current;
    }
    current--;
  }

  return 1;
}



