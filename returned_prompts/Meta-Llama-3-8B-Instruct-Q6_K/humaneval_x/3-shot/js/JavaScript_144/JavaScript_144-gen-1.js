  const [xNumerator, xDenominator] = x.split('/').map(Number);
  const [nNumerator, nDenominator] = n.split('/').map(Number);

  const gcd = (a, b) => {
    if (b === 0) {
      return a;
    }
    return gcd(b, a % b);
  };

  const resultNumerator = xNumerator * nDenominator;
  const resultDenominator = xDenominator * nNumerator;

  const gcdResult = gcd(resultNumerator, resultDenominator);

  return resultNumerator / gcdResult === resultDenominator / gcdResult;
}