  const unitDigitMultiplier = (num) => {
    return num % 10;
  };

  const aUnitDigit = unitDigitMultiplier(a);
  const bUnitDigit = unitDigitMultiplier(b);

  return aUnitDigit * bUnitDigit;
}

