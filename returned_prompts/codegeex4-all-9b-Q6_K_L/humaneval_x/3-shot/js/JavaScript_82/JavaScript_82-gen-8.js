  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i < Math.sqrt(n) + 1; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  return isPrime(string.length);
}