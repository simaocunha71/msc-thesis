  let factors = [];
  let copy = a;
  for (let i = 2; i <= Math.sqrt(copy); i++) {
    while (copy % i === 0) {
      factors.push(i);
      copy /= i;
    }
  }
  if (copy > 1) {
    factors.push(copy);
  }
  if (factors.length === 3 && factors.every(isPrime)) {
    return true;
  }
  return false;
}

const isPrime = (n) => {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}


