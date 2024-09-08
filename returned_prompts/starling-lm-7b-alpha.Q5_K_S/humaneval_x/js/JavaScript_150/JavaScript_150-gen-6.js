  const isPrime = (number) => {
    if (number < 2) return false;
    for (let i = 2; i * i <= number; i++) {
      if (number % i === 0) return false;
    }
    return true;
  }

  if (isPrime(n)) return y;
  return x;
}



