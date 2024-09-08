  let result = 0;
  for (let i = 0; i < num.length; i++) {
    if (hexPrimes(num[i]) !== undefined) {
      result += 1;
    }
  }
  return result;
}

/*
  >>> countPrimes('AB')
  1
  >>> countPrimes('1077E')
  2
  >>> countPrimes('ABED1A33')
  4
  >>>