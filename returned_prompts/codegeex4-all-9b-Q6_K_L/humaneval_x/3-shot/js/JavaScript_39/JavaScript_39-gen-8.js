  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i < Math.sqrt(n); i++) {
      if (n % i == 0) return false;
    }
    return true;
  }

  let fibs = [0, 1];
  let current = 1;
  while (fibs.length < n) {
    let next = fibs[fibs.length - 1] + fibs[fibs.length - 2];
    if (isPrime(next)) fibs.push(next);
    fibs.push(next);
    current += 1;
  }

  return fibs[n];
}



