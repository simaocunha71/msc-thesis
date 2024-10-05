  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }

  let result = [];
  for (let i = 0; i < n; i++) {
    if (isPrime(i)) {
      result.push(i);
    }
  }

  return result;
}



