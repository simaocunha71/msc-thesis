const isMultiplyPrime = (a) => {
  const prime = [2, 3, 5];
  let b = a;
  for (let i = 0; i < prime.length; i++) {
    let c = prime[i];
    if (b % c === 0) {
      if (b / c >= 100) return false;
      b /= c;
    } else {
      return false;
    }
  }
  return true;
};

