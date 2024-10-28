  let primeFactors = [];
  let count = 0;
  for (let i = 2; i <= a; i++) {
    if (a % i == 0) {
      primeFactors.push(i);
      a = a / i;
      i--;
    }
  }
  for (let i = 0; i < primeFactors.length; i++) {
    for (let j = 0; j < primeFactors.length; j++) {
      if (primeFactors[i] == primeFactors[j] && i != j) {
        count += 1;
      }
    }
  }
  if (count > 2) {
    return false;
  }
  return true;
}



